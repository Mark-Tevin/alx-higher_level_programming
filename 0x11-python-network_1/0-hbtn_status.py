#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf-8 content: {}".format(body.decode("utf-8")))
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e.reason}")
