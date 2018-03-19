# -*- coding utf-8 -*-
#!/usr/bin/env python3

import sys

zero = ['  *  ', ' * * ', '*   *', '*   *', '*   *', ' * * ', '  *  ']
one = [' * ', '** ', ' * ', ' * ', ' * ', ' * ', '***']
two = [' *** ', '*   *', '*  * ', '  *  ', ' *   ', '*    ', '*****']
three = [' *** ', '*   *', '   * ', ' *** ', '   * ', '*   *', ' *** ']
four = ['   * ', '  ** ', ' * * ', '*  * ', '*****', '   * ', '   * ']
five = ['****', '*   ', '*** ', '   *', '   *', '   *', '*** ']
six = ['  **', ' *  ', '*   ', '* * ', '*  *', '*  *', '*** ']
seven = ['*****', '    *', '   * ', '  *  ', ' *   ', '*    ', '*    ']
eight = [' *** ', '*   *', '*   *', ' *** ', '*   *', '*   *', ' *** ']
nine = [' *** ', '*   *', '*   *', ' ****', '    *', '    *', '   * ']
Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

s = input('Enter an int:')

try:
    row = 0
    while row < 7:
        line = ''
        for i in range(len(s)):
            num = int(s[i])
            digit = Digits[num]
            for j in range(len(digit[0])):          #每行单个元素取值
                s1 = digit[row]
                if s1[j] == ' ':
                    line += s1[j]
                else:
                    line += s[i]
            line += '  '
        print(line)
        row += 1
except IndexError:
    print('usage:bigdigits.py <number>')
except ValueError as err:
    print(err, 'in', digits)