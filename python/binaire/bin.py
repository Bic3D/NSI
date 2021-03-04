def binary(num):
    binary = ""
    
    while num > 0:
        bit = num%2
        binary = str(bit) + binary # on rajoute le bit au nombre en binaire mais à la fin parce que comme ça ça inverse l'ordre
        num = num//2

    return binary