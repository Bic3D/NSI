import turtle
import math

bob = turtle.Turtle()
#bob.hideturtle()

def rectangle(arraySides):
    """
    rectangle(arraySides)
    arraySides:   array, un array qui contient la longueur et la largeur.

    ex: rectangle([50, 100])
    """
    for i in range(4):
        bob.left(90)
        bob.forward(arraySides[i%2])

def polygone(cotes, longueur):
    """
    polygone(arraySides)
    cotes:    le nombre de côtés
    longueur: la longueur d'un côté

    crée un polygone régulier de 'cotes' cotés et de longueur  'longueur'
    ex: polygone(6, 40)
    """
    for i in range(cotes):
        bob.left(360/cotes)
        bob.forward(longueur)

def etoile():
    for i in range(6):
        bob.left(60)
        bob.forward(50)
        bob.backward(50)

def truc():
    bob.goto(20, 0)
    bob.goto(0, 20)
    bob.goto(20, 20)
    bob.goto(0, 0)
    bob.goto(0, 20)
    bob.goto(10, 30)
    bob.goto(20, 20)
    bob.goto(20, 0)


def bizarre(index):
    if index == 1:
        bob.begin_fill()

        bob.left(45)
        bob.forward(100)
        bob.right(180-30)
        bob.forward((200*math.sqrt(3))/3)
        bob.right(180-(180-30-90))
        bob.forward(100+(100*math.sqrt(3))/3)

        bob.left(180-30)
        bob.forward((200*math.sqrt(3))/3)
        bob.left(120)
        bob.forward((100*math.sqrt(3))/3)

        bob.end_fill()

    elif index == 2:
        bob.begin_fill()

        for i in range(0, 3):
            for i in range(0, 3):
                bob.forward(100)
                bob.left(120)
            bob.left(120)

        bob.end_fill()

    elif index == 3:
        bob.color("#c7bf30","#f2e827")
        bob.begin_fill()

        for i in range(0, 3):
            bob.forward(200)
            bob.left(120)
        bob.forward(100)
        bob.left(60)
        for i in range(0, 3):
            bob.forward(100)
            bob.left(120)

        bob.end_fill()
    
    elif index == 4:
        bob.begin_fill()
        for i in range(0, 36):
            bob.forward(10)
            bob.right(10)
        
        
        for i in range(0, 18):
            bob.forward(5)
            bob.right(10)
        for i in range(0, 18):
            bob.forward(5)
            bob.left(10)
        
        bob.end_fill()

"""
rectangle([50, 100])

bob.penup()
bob.forward(100)
bob.pendown()

polygone(6, 40)

bob.penup()
bob.forward(100)
bob.pendown()

etoile()
"""
bizarre(4)

input("appuyez sur Entrée pour fermer la fenêtre")