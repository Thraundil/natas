# Natas1 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas1.natas.labs.overthewire.org/"

auth_name = 'natas1'
auth_pass = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
# ***********************************************

r = requests.get(URL, auth=(auth_name, auth_pass))

# The password is simply stored as a comment in the HTML
for x in r.iter_lines():
    if "The password" in x:
        print x