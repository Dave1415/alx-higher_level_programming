#!/bin/bash
#sends a GET request to the URL with header variable
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
