#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


def do_pack():
    """ A function that compresses the files before sending"""

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    archive_name = f"web_static_{year}{month}{day}{hour}{minute}{second}.tgz"
    local('mkdir -p versions')
