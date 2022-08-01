#!/usr/bin/python3
"""Module containing inherits_from method"""


def inherits_from(obj, a_class):
    """returns True if object is an instance of a class that
    inherited (directly or indirectly) from specified class;
    otherwise False"""
    return isinstance(obj, a_class) and type(obj) != 
