#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests

if __name__ == '__main__':
    URL = argv[1]
    req = requests.get(URL)
    print(req.headers.get('X-Request-Id'))
