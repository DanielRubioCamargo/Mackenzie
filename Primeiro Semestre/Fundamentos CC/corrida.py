import turtle
from random import randint, choice
from time import sleep

def setTurtles(amount, turtles, colors):
    initialPos = 150
    for i in range(amount):
        t = turtle.Turtle()
        t.speed(8)
        chosenColor = choice(colors)
        t.color(chosenColor)
        colors.remove(chosenColor)
        t.shape("turtle")
        t.left(90)
        t.forward(initialPos)
        t.left(90)
        t.forward(200)
        t.left(180)
        initialPos -= 30
        t.clear()
        turtles.append(t)

def drawSquare(size, color, x, y):
    t = turtle.Turtle()
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.speed(10)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()
    t.home()

def startRace(turtles):
    finalXpos = 0
    finalYpos = 0
    canBreak = False
    while True:
        if canBreak:
            break
        for i in turtles:
            if i.pos()[0] > 200:
                finalXpos = i.pos()[0] + 25
                finalYpos = i.pos()[1] - 5
                canBreak = True
                break
            v = randint(0,30)
            i.forward(v)
        sleep(0.2)
    drawSquare(10, "yellow", finalXpos, finalYpos)

turtlesList = list()
colors = ["red","green","orange","blue","yellow"]
amount = len(colors)

setTurtles(amount, turtlesList, colors)
startRace(turtlesList)

turtle.done()
