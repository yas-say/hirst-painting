import colorgram as c
from turtle import Turtle, Screen
from random import choice


def getcolor(colorsObj):
    mycolorlist = []
    for item in colorsObj:
        rgb = item.rgb
        tup = (rgb.r, rgb.g, rgb.b)
        mycolorlist.append(tup)
    return mycolorlist


def createpainting(x, y, c):
    for a in range(x):
        for b in range(y):
            tim.pendown()
            tim.dot(10, choice(c))
            tim.penup()
            # print(f"{a} : {b*10}")
            tim.setpos(a * 20, b * 20)
    tim.dot(10, choice(c))

colors = c.extract("hirst.jpg", 100)
# print(len(colors))
# print(colors)

colorlist = getcolor(colors)

# print(colorlist)

tim = Turtle()
tim.hideturtle()
tim.speed(0)
screen = Screen()
screen.colormode(255)
createpainting(10, 10, colorlist)

screen.exitonclick()
