#!/usr/bin/python3
"""A module that compresses files before sending
   All files in the folder web_static must be added to the final archive
   Store all archives in the folder versions(create if it doesn’t exist)
   Create archives like web_static_<year><month><day><hour><minute><second>.tgz
   The function do_pack must return the archive path if the
   archive has been correctly generated. Otherwise, it should return None
"""
from fabric.api import local, task
from datetime import datetime


@task
def do_pack():
    """A function that compresses the files before sending"""

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    archive_name = f"web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    local('mkdir -p versions')
    try:
        local(f'tar -cvzf versions/{archive_name} web_static')
        return f'versions/{archive_name}'
    except Exception as e:
        return None
