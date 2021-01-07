# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

annee2 = 2048

def nom():
    name = input("\n************************************************************\nSalut, comment tu t'appelles?\n> ")
    
    year = int(input("Alors bonjour " + name + ", en quelle année est-tu né? (il faut avoir 21 ans pour rentrer)\n> "))
    
    age = annee2 - year
    
    if year == 21:
        print("mmmmmmh... apparemment t'as lu un peu trop vite!\nET TU AS ESSAYE DE M'ARNAQUER GROS TRICHEUR!!")
        return
    
    if age < 0:
        print("Mais... ce n'est pas possible!!")
        return
    #else:
    #    print("Tu auras " + str(age) + " ans en " + str(annee2) + ".")
        
    elif age > 21:
            print("Ok c'est bon tu peux rentrer!")
    else:
        print("TU N'AS PAS LE DROIT D'ETRE ICI!!! TU ES TROP JEUNE")




def trucdemaximilien():
    print("turtle is coming")
    

#nom()
    
    
    
def pair(nombre):
    if (nombre%2) == 0:
        return "pair"
    else:
        return "impair"


nbr = int(input("Choisis un nombre: "))
print(str(nbr)+" est "+ pair(nbr))