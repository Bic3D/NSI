# -*- coding: utf-8 -*-

def rectangle(longueur, largeur):
    """
    rectangle(float longueur, float largeur)
    longueur:   float, la longueur du rectangle
    largeur:    float, la largeur du rectangle
    retourne un float contenant l'aire du rectangle
    """
    aire = longueur * largeur
    return aire


def prixTTC(prix):
    """
    rectangle(float prix)
    prix:   float, la longueur du rectangle
    retourne un float contenant le prix TTC
    """
    tax = prix * 1.206
    return tax

print(rectangle(5, 8))
