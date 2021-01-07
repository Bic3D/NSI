import turtle
import math
import random
import formes

colors = ["red","yellow","green","blue","orange","black"]
colorList = random.randint(0,255), random.randint(0,255), random.randint(0,255)

r = lambda: random.randint(0,255)
randomHex = lambda: '#%02X%02X%02X' % (r(),r(),r())


bob = turtle.Turtle()

#turtle.colormode(255)

bob.color(randomHex(), randomHex())

sides = [200, 300]
hypo = 200
base = 100

bob.pensize(5)

bob.hideturtle()
bob.penup()
bob.forward(-sides[0]/2)
bob.right(90)
bob.forward(sides[1]/2)
bob.right(-90)
bob.pendown()
bob.showturtle()

for i in range(0, 4):
    bob.forward(sides[i % 2])
    bob.left(90)

#formes.polygone(8, 100, bob)

bob.hideturtle()
bob.penup()
bob.forward(sides[0]/2)
bob.right(-90)
bob.forward(sides[1]/2)
bob.right(90)

angle = math.degrees(math.asin(base/hypo))  # je calcule l'angle avec le sinus
hauteur = math.sqrt(hypo**2 - base**2)

bob.forward(-base/2)
bob.right(90)
bob.forward(hauteur/2)
bob.right(-90)
bob.pendown()
bob.showturtle()

#bob.color("#a3a3a3","#DCD579")

#bob.color(random.choice(colors))
#bob.color(colorList)

bob.speed(0)

def tournermegavite():
    bob.fillcolor(randomHex())

    bob.begin_fill()
    bob.forward(base)
    bob.left(90+angle)
    bob.forward(hypo)
    bob.right(90+angle)
    bob.forward(base)
    bob.right(90+angle)
    bob.forward(hypo)
    bob.end_fill()
    bob.left(120)

    bob.forward(-2)

bob.hideturtle()
while True:
    tournermegavite()
