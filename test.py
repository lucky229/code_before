#! usr/bin/env python
# -*- coding:utf-8 -*-

import random

blue = []
num = 5

while len(blue) < num+1:
    a = random.randint(1,36)
    if a not in blue:
        blue.append(a)

print('Blue is :', sorted(blue))
print('Red is :', random.randint(1,16))