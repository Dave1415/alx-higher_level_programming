#!/bin/bash
#requste the head and display the size of the body
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
