#!/usr/bin/env python3

import os
import json

from templates import login_page

# Create an empty directory
envs = {}

# Iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    envs[env_key] = env_value

# Dumps env variables as json
print("Content-Type: text/html")
print()

print(login_page())

# Question 2
# print(envs["QUERY_STRING"])

# Question 3
# print(envs["HTTP_USER_AGENT"])
