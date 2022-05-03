#!/usr/bin/python3
variable = 97
while (variable < 123):
    if(variable == 113 or variable == 101):
        variable += 1
        continue
    print(chr(variable), end='')
    variable += 1
