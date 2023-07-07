#!/usr/bin/python3
"""
a python script Fab module to create a targ file of all my static files
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function to pack in .tgz
    """
    local("mkdir -p versions")
    now = datetime.today()
    try:
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                         now.day, now.hour,
                                                         now.minute,
                                                         now.second)
        local("tar -cvzf versions/{} web_static".format(file_name))
        return (file_name)
    except exception:
        return (None)
