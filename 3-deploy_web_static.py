#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive
"""
from fabric.api import *
from datetime import datetime
import os.path

env.user = 'ubuntu'
env.hosts = ['54.157.189.192', '107.22.144.60']


def do_pack():
    """a function that generates a .tgz archive
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/web_static_{}.tgz web_static/".
                    format(time))
    if archive:
        return ("versions/web_static_{}.tgz".format(time))
    else:
        return None


def do_deploy(archive_path):
    """a function that deploys an archive
    """
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        link = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm /tmp/{}'.format(archive))
        run('rm -rf {}'.format(link))
        run('ln -s {} {}'.format(path, link))
        print('New version deployed!')
        return True
    else:
        return False


def deploy():
    """Creates and distributes and archive to a server"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
