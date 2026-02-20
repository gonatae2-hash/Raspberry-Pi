#!/usr/bin/python3
import os
import sys
import urllib.parse

print("Content-Type: text/html\n")

length = int(os.environ.get("CONTENT_LENGTH", 0))
data = sys.stdin.read(length)
params = urllib.parse.parse_qs(data)

login_id = params.get("loginid", [""])[0]

print("<html>")
print("<body>")
print(f"<h2>Hello {login_id}</h2>")
print("</body>")
print("</html>")