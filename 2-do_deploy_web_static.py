#!/usr/bin/python3
"""Deploy web_static to remote servers"""
from datetime import datetime
from fabric.api import *
from os import path


# Set the remote hosts, username and key file to use for authentication
env.hosts = ['52.201.228.252', '34.204.61.36']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa_sandbox'


def do_deploy(archive_path):
    """Deploy compressed archive containing web files to remote servers"""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing sym_link
        run('sudo rm -rf /data/web_static/current')

        # re-establish sym_link
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except BaseException:
        return False

    # return True on success
    print("New version deployed!")
    return True
