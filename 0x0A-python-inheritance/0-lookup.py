#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """Lookup method
    Returns: list of available attributes, methods of object"""
    return dir(obj)
