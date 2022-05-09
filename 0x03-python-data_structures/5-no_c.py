#!/usr/bin/python3
def no_c(my_string):
    # creamos una string que no va a contener "C" ni "c"
    string_without_C = ""
    # creamos un ciclo for que recorra cada caracter de la string
    # despues auto agregamos el caracter si no tiene la C
    # y retornamos la nueva string sin la C
    for char in my_string:
        if char != 'c' and char != 'C':
            string_without_C += char
    return string_without_C
