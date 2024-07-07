#!/bin/bash
# script that takes a URL, sends a request to the URL, and displays the size of the body of the response
curl -s "$1" | wc -c 
