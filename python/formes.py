import turtle

def rectangle(arraySides, bob):
    """
    rectangle(arraySides)
    arraySides:   array, un array qui contient la longueur et la largeur.
    bob:          la turtle a utiliser

    ex: rectangle([50, 100], bob)
    """

    pos = bob.pos()
    for i in range(4):
        bob.left(90)
        bob.forward(arraySides[i%2])

    bob.hideturtle()
    print(pos)
    bob.showturtle()

def polygone(cotes, longueur, bob):
    """
    polygone(arraySides)
    cotes:    le nombre de côtés
    longueur: la longueur d'un côté
    bob:      la turtle a utiliser

    crée un polygone régulier de 'cotes' cotés et de longueur  'longueur'
    ex: polygone(6, 40, bob)
    """

    pos = bob.pos()
    for i in range(cotes):
        bob.left(360/cotes)
        bob.forward(longueur)

    bob.hideturtle()
    print(pos)
    bob.showturtle()

def etoile(bob):
    for i in range(6):
        bob.left(60)
        bob.forward(50)
        bob.backward(50)