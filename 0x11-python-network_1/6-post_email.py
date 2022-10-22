#!/usr/bin/python3
"""
takes URL and email address, sends POST request to passed URL
with email as parameter, and finally displays body of response
"""


import requests
from sys import argv


if __name__ == '__main__':
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
