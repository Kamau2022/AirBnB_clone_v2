#!/usr/bin/python3
"""This module will distribute archive file to
   webservers
"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ['107.22.144.60', '54.157.189.192']


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
        run('ln -s {} {}'.format(file_archive), link)
        return True
    else:
        return False
