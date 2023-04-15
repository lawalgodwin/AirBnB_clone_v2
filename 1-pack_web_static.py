#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


def do_pack():
    """ A script that generates archive the contents of web_static folder"""

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
