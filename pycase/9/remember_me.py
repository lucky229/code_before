#！/usr/bin/env python3
# -*- coding utf-8 -*-   180

import json

filename = "text_file\\username.json"
try:
    with open(filename) as f_object:
        name = json.load(f_object)
except FileNotFoundError:
    username = input("Enter your name: ")
    filename = 'text_file\\username.json'
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
        print("We'll remember you when you come back, " + username.title() + "!")
else:
    print("Welcome back, " + name.title() + "!")