#!/usr/bin/python3
from datetime import date
from fabric.api import local
from time import strftime


def do_pack():
    """
    Creates a compressed archive of the contents of the web_static directory.
    The resulting archive is stored in a subdirectory called versions,
    and the filename includes the current date and time.
    Returns the path to the created archive on success, or None on failure.
    """

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
