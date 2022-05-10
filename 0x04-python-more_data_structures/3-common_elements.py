#!/usr/bin/python3
def common_elements(set_1, set_2):

    # set() lo estamos utilizando para encontrar
    # un elemento en comun entre 2 listas

    Set1 = set(set_1)
    Set2 = set(set_2)
    setcomun = Set1 & Set2
    return setcomun
