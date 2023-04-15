#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
import os


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

    return 'versions/{}'.formart(archive_name)
