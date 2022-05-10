#!/usr/bin/python3
def common_elements(set_1, set_2):

    Set1 = set(set_1)
    Set2 = set(set_2)
    # & compara las 2 listas y nos retorna el valor duplicate
    setcomun = Set1 & Set2
    return setcomun
