import turtle

t = turtle.Turtle()
t.speed(0)

table =  [[0,0,0,2,2,2,2,2,2,0,0,0,0],
[0,0,2,2,2,2,2,2,2,2,2,2,0],
[0,0,6,6,6,3,3,3,1,3,0,0,0],
[0,6,3,6,3,3,3,3,1,3,3,3,0],
[0,6,3,6,6,3,3,3,3,1,3,3,3],
[0,6,6,3,3,3,3,3,1,1,1,1,0],
[0,0,0,3,3,3,3,3,3,3,3,0,0],
[0,0,2,2,5,2,2,2,2,0,0,0,0],
[0,2,2,2,5,2,2,5,2,2,2,0,0],
[2,2,2,2,5,5,5,5,2,2,2,2,0],
[3,3,2,5,4,5,5,4,5,2,3,3,0],
[3,3,3,5,5,5,5,5,5,3,3,3,0],
[3,3,5,5,5,5,5,5,5,5,3,3,0],
[0,0,5,5,5,0,0,5,5,5,0,0,0],
[0,6,6,6,0,0,0,0,6,6,6,0,0],
[6,6,6,6,0,0,0,0,6,6,6,6,0]]

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
            elif j == 3:
                c = "#F7C192"
            elif j == 4:
                c = "#FDFD11"
            elif j == 5:
                c = "#0071C1"
            else:
                c = "#9D4700"
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