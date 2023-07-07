#!/usr/bin/python3
"""
a python script Fab module to create a targ file of all my static files
"""
from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path
env.hosts = ['54.157.154.38', '54.157.154.38']


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
    except:
        return (None)


def do_deploy(archive_path):
    """
    logic to deploy into ssh servers
    """
    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        directory_path = archive_path.split(".")[0]
        directory_path = directory_path.split("/")[-1]
        archive_path = archive_path.split("/")[-1]
        sudo("mkdir -p /data/web_static/releases/{}/".format(directory_path))
        full_path = "/data/web_static/releases/{}".format(directory_path)
        sudo("tar -xvzf /tmp/{} -C {}".format(archive_path, full_path))
        sudo("rm -rf /tmp/{}".format(archive_path))
        sudo("mv -f {}/web_static/* {}".format(full_path, full_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf {} /data/web_static/current".format(full_path))
        return(True)
    except:
        return(False)
