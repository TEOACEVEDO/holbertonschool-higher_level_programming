#!/usr/bin/python3
from sys import argv
t = 1
suma = 1

while t < len(argv):
    suma += int(argv[t])
    t += 1

print(suma)
