#!/bin/bash
# display the status code
curl -sI "$1" -o /dev/null -w '%{http_code}'
