#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """a function that generates a .tgz archive
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static/".
                    format(time))
    if archive:
        return ("versions/web_static_{:s}.tgz".format(time))
    else:
        return None
