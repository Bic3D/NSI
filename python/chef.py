# -*- coding: utf-8 -*-

import random
import time

chefs = ["Jackie","Frédéric","Albert","Jean-Louis Auguste","Alphonse","Pauline","Sulimane","François","Maximus Robespierus","Arturette","Tartiflette","Alain","je suis une string","xXSuperCuisinierXx"]
chefs_pas_elus = []

def chooseChief():
    global chefs_pas_elus
    
    if (set(chefs_pas_elus) == set(chefs)):
        print("\nTout le mone a été élu donc on recommence")
        chefs_pas_elus = []

    while True:
        current_chef = random.choice(chefs)

        if current_chef not in chefs_pas_elus:
            chefs_pas_elus.append(current_chef)
            break

    return current_chef

while True:
    print("Cette année, le chef élu est... "+chooseChief()+"!")
    time.sleep(0.5)