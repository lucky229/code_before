#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    numbers = []
    sum = 0
    count = 0
    lowest = 0
    highest = 0

    while True:
        s = input('enter a number or Enter to finish:')
        num = int(s)
        if num or num == 0:
            numbers += s
            count += 1
            if num > highest:
                highest = num
            if num < lowest:
                lowest = num
    print('count = ', count, 'sum = ', sum, 'lowest = ', lowest, 'highest = ', highest, 'mean = ', sum/count)

except ValueError as err:
    print(err)