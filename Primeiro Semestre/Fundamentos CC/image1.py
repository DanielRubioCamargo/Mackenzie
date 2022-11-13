import turtle

t = turtle.Turtle()
t.speed(0)

table =  [[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
[0,0,0,1,1,0,0,2,2,0,0,1,1,0,0,0],
[0,0,1,0,0,0,2,2,2,2,0,0,0,1,0,0],
[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
[0,1,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
[1,0,0,2,2,0,0,0,0,0,0,2,2,0,0,1],
[1,0,2,2,2,2,0,0,0,0,2,2,2,2,0,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,1],
[0,1,1,1,3,3,1,3,3,1,3,3,1,1,1,0],
[0,0,1,3,3,3,1,3,3,1,3,3,3,1,0,0],
[0,0,1,3,3,3,3,3,3,3,3,3,3,1,0,0],
[0,0,0,1,3,3,3,3,3,3,3,3,1,0,0,0],
[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0]
]

def drawSquare(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def drawImage(tb, pxSize):
    c = ""
    initialX = 0
    initialY = 0
    for i in tb:
        for j in i:
            if j == 0:
                c = "#ffffff"
            elif j == 1:
                c = "#000000"
            elif j == 2:
                c = "#F80500"
            else:
                c = "#F7C192"
            drawSquare(pxSize,c)
            t.penup()
            t.forward(pxSize)
            t.pendown()
        t.penup()
        t.home()
        initialY -= pxSize
        t.sety(initialY)
        t.pendown()

drawImage(table, 5)
turtle.done()

