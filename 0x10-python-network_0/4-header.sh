#!/bin/bash
#sends a GET request to the URL with header variable
curl -sH "X-School-User-Id: 98" "$1"
