#!/usr/bin/env python3

import cgi
import os
import secret
import json

from templates import login_page, secret_page

logged_in = False
body = ""
header = ""

# Check for cookies
if "HTTP_COOKIE" in os.environ:
    cookies = os.environ["HTTP_COOKIE"].split(";")
    if "logged=true" in cookies:
        logged_in = True


form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

# Question 4
# print("Content-Type: text/html")
# print()
# print("<p>Username:", form["username"].value)
# print("<p>Password:", form["password"].value)


header = "Content-Type: text/html\r\n"

if logged_in:
    body += secret_page(secret.username, secret.password)
elif (username == secret.username and password == secret.password):
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<p>Username: {}".format(secret.username)
    body += "<p>Password: {}".format(secret.password)
else:
    body += "<p>Username: {}".format(username)
    body += "<p>Password: {}".format(password)

print(header)
print()
print(body)