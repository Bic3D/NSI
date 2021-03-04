# -*- coding: utf-8 -*-

def binary(num):
    """
    Returns the converted integral to binary in a string
    """
    binary = ""
    
    while num > 0:
        bit = num%2
        binary = str(bit) + binary # on rajoute le bit au nombre en binaire mais à la fin parce que comme ça ça inverse l'ordre
        num = num//2

    return binary

def utf8(num):
    """
    Returns the amount of bytes needed to convert the number (num) to utf-8 in a string
    """
    # code de la prof louche
    if num < 8:
        return 1
    else:
        return num//6+1

    return binary