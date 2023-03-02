#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ a function that generates .tgz archive
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p ./versions")
    archive = local("tar -czvf versions/web_static_{}\
                    .tgz web_static".format(now))
    if archive:
        return ("versions/web_static_{}".format(now))
    else:
        return None
