#!/usr/bin/python3

from fabric.api import local
from datetime import datetime


def do_pack():
    """ A function that compresses the files before sending"""

    now = datetime.now()
