import turtle

t = turtle.Turtle()
t.pencolor("black")
t.shape("classic")

def drawRect(sizeX, sizeY, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(sizeX)
        t.left(90)
        t.forward(sizeY)
        t.left(90)
    t.end_fill()

def drawTri(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def drawThing(sizeX, sizeY, angle, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(sizeX)
        t.left(angle)
        t.forward(sizeY)
        t.left(180-angle)
    t.end_fill()

drawRect(100,70, "red")
t.penup()
t.setx(40)
t.pendown()
drawRect(20,30, "black")
t.penup()
t.setx(100)
t.pendown()
drawRect(200,70,"red")
t.penup()
t.setpos(160,20)
t.pendown()
drawRect(40,20,"black")
t.penup()
t.setpos(210,20)
t.pendown()
drawRect(40,20,"black")
t.penup()
t.home()
t.sety(70)
t.pendown()
drawTri(100,"orange")
t.penup()
t.setx(100)
t.pendown()
drawThing(200,100,120,"orange")

turtle.done()