#！/usr/bin/env python3
# -*- coding utf-8 -*-   180

print("Give two numbers, we can plus them.")
print("Enter '9999' to quit at any time.")

while True:
    try:
        first_number = int(input("First number: "))
        if first_number == 9999:
            break
        secend_number = int(input("Secend number: "))
        if secend_number == 9999:
            break
    except ValueError:
        print("Enter a number ,please!")
    else:
        sum = first_number + secend_number
        print("The sum is " + str(sum) +  " .")