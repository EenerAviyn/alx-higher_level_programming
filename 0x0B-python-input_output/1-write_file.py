#!/usr/bin/python3
"""Module with function that writes string to text file"""


def write_file(filename="", text=""):
    """writes string to text file and returns number of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
