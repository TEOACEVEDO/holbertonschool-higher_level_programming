#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    t, suma = 1, 0

    while t < len(argv):
        suma += int(argv[t])
        t += 1

    print(suma)
