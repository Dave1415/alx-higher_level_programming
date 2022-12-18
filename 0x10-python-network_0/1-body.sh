#!/bin/bash
# send a GET request and displays the body if response code is 200
curl -sL -X GET "$1"
