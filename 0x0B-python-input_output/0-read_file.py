#!/usr/bin/python3
"""Module containing function for reading txt file(UTF8)"""


def read_file(filename=""):
    """Method that reads text file (UTF8) and prints it to stdouts"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
