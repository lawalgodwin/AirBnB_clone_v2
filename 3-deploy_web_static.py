#!/usr/bin/python3
"""A module that archives and deploy to the server"""

from fabric.api import local, run, env, put, sudo
from datetime import datetime
import os.path

env.hosts = ['54.144.198.110', '54.152.132.248']
env.user = 'ubuntu'


def do_pack():
    """ A function that compresses the files before sending"""

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    local('mkdir -p versions')
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        year, month, day, hour, minute, second)

    try:
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return 'versions/{}'.format(archive_name)
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Deploy an archive to the remote server"""
    try:
        print("Deploying archive....")

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp", use_sudo=True)
        # Uncompress it into the folder /data/web_static/releases/
        # /data/web_static/releases/<archive filename without extension>
        basename = os.path.basename(archive_path)
        run('mkdir -p /data/web_static/releases/{}'
            .format(basename.split('.')[0]))
        run('tar -xzvf /tmp/{} -C /data/web_static/releases/{}'
            .format(basename, basename.split('.')[0]))
        # delete the archive from the web server
        run('rm /tmp/{}'.format(basename))
        # Delete the symbolic link /data/web_static/current on web server
        # Create a new the symbolic link /data/web_static/current on the
        # web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        server_data_point = "data/web_static/releases"
        sudo('mv /{0}/{1}/web_static/* /{0}/{1}/'
             .format(server_data_point, basename.split('.')[0]))
        sudo('rm -rf /data/web_static/releases/{}/web_static'
             .format(basename.split('.')[0]))
        run('sudo mkdir -p /data/web_static/current')
        run('sudo rm -rf /data/web_static/current')
        run('sudo mkdir -p /data/web_static/current')
        run('sudo ln -sf /{0}/{1}/* /data/web_static/current/'
            .format(server_data_point, basename.split('.')[0]))
        return True
    except Exception as e:
        print("Error: ", e)
        return False


def deploy():
    """Fully deploy the code"""
    # Prepare the archive
    archive_path = do_pack()
    if (not os.path.exists(archive_path)):
        return False
    do_deploy(archive_path)
