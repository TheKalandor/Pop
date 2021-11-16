import turtle
import random
print("hello")
maTortue4 = turtle.Turtle()
maTortue4.color("blue")
maTortue1 = turtle.Turtle()
maTortue1.color("red")
maTortue2 = turtle.Turtle()
maTortue2.color("purple")
maTortue3 = turtle.Turtle()
maTortue3.color("orange")

#cours 
"""maTortue.forward(100)
maTortue.speed(0.1)
turtle.delay(0)

maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)
input()"""

#cercle
"""turtle.delay(0)
maTortue.speed(0)
for i in range(1,360,1):
    maTortue.left(1)
    maTortue.forward(1)
input()"""


#carre
"""turtle.delay(0)
maTortue.speed(0)
for i in range(1,5,1):
    maTortue.left(90)
    maTortue.forward(50)
input()"""

#escargot carre
"""turtle.delay(0)
maTortue.speed(0)
for i in range(300):
    maTortue.left(90)
    maTortue.forward(0+i*2)

input()"""

#escargot cercle
"""turtle.delay(0)
maTortue.speed(0)
for i in range(900):
    maTortue.left(1)
    maTortue.forward(0+i/250)

input()"""


#tortue qui avance
turtle.delay(0)
def Nmb (tortue1,tortue2,tortue3,tortue4):
    while 1:
        pas(tortue1)
        pas(tortue2)
        pas(tortue3)
        pas(tortue4)

def pas (tortu):
    tortu.speed(0)
    var = random.randint(1,3)
    #maTortue.forward(3)
    #for i in range(0,4):
    if var == 1:
        tortu.left(90)
        tortu.forward(10)
    elif var == 2:
        tortu.right(90)
        tortu.forward(10)
    else :
        tortu.forward(10)


Nmb(maTortue4,maTortue3,maTortue2,maTortue1)





