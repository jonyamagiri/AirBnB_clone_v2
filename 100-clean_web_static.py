#!/usr/bin/python3
import os
from fabric.api import *

# Set the remote hosts, username and key file to use for authentication
env.hosts = ['52.201.228.252', '34.204.61.36']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa_sandbox'


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
