#!/usr/bin/python3
"""Module with function that appends string to text file"""


def append_write(filename="", text=""):
    """Mtd that appends string to text file and returns no.\
        of chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
