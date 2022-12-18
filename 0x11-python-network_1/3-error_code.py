#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

from urllib import request, error
from sys import argv

if __name__ == '__main__':
    URL = argv[1]
    try:
        with request.urlopen(URL) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
