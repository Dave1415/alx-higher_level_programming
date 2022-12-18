#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests

if __name__ == '__main__':
    URL = 'https://intranet.hbtn.io/status'
    req = requests.get(URL)
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
