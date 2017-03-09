"""Utils library"""
from subprocess import call
import sys

def execute(cmd):
    """Execute a command

    Args:
        cmd: a shell command

    Return:
        None
    """
    call(cmd.split(' '))


def delete_dir(argv, parent=''):
    """Delete one or more dirs

    Args:
        argv: string or list with names to be added

    Return:
        is_created: bool
    """
    # If is a string, just pcreate a dir
    if type(argv) == type(''):
        execute('rm -r ' + argv)

    elif type(argv) == type([]):
        execute('rm -r ' + ' '.join(argv))


def create_dir(argv, parent=''):
    """Create one or more dirs

    Args:
        argv: string or list with names to be added

    Return:
        is_created: bool
    """
    # If is a string, just pcreate a dir
    if type(argv) == type(''):
        call(['mkdir', '-p', argv])

    elif type(argv) == type([]):
        for i in argv:
            create_dir(i)


def is_int(arg):
    """ Check if type is int

    Args:
        Some value

    Return:
        True or False"""
    return bool(type(arg) == type(0))


def is_bool(arg):
    """ Check if type is bool

    Args:
        Some value

    Return:
        True or False"""
    return bool(type(arg) == type(True))


def is_string(arg):
    """ Check if type is string

    Args:
        Some value

    Return:
        True or False"""
    return bool(type(arg) == type(''))


def is_list(arg):
    """ Check if type is list

    Args:
        Some value

    Return:
        True or False"""
    return bool(type(arg) == type([]))


def is_oject(arg):
    """ Check if type is oject

    Args:
        Some value

    Return:
        True or False"""
    return bool(type(arg) == type({}))
