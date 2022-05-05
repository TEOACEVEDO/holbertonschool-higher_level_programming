#!/usr/bin/python3
from sys import argv
t, suma = 1, 0

while t < len(argv):
    suma += int(argv[t])
    t += 1

print(suma)
