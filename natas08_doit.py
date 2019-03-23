# Natas8 python solution
# By Emil 'Dota' Bak, 2019

import requests, base64

# ***********************************************
URL = "http://natas8.natas.labs.overthewire.org"

auth_name = 'natas8'
auth_pass = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************


# The encrypted secret can be found in the visible source-code
ENCRYPTED_SECRET = "3d3d516343746d4d6d6c315669563362"

# To decode the secret, the user must reverse the order of encryption
def decodeSecret(secret):
    return base64.b64decode((secret.decode("hex"))[::-1])

DATA = dict(secret=decodeSecret(ENCRYPTED_SECRET), submit="submit")

r = s.post(URL, data=DATA)

for x in r.iter_lines():
    if "password" in x:
        print x