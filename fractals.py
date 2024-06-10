import turtle
import random
window = turtle.Screen()
window.setup(600, 600)
window.colormode(255)

def koch_curve(t, depth, size):
    if (depth == 1):
        t.fd(size)
    else:
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
        t.rt(120)
        koch_curve(t, depth-1, size)
        t.lt(60)
        koch_curve(t, depth-1, size)
def koch_curve2(t, depth, size, w):
    t.width(w)
    if (depth == 1):
        t.fd(size)
    else:
        t.pencolor("green")
        koch_curve2(t, depth-1, size, w)
        t.lt(75)
        t.pencolor("green")
        koch_curve2(t, depth-1, size, w)
        t.rt(150)
        t.pencolor("white")
        koch_curve2(t, depth-1, size, w)
        t.lt(75)
        t.pencolor("green")
        koch_curve2(t, depth-1, size, w)
        t.lt(75)
        t.pencolor("green")
        koch_curve2(t, depth-1, size, w)
        t.rt(150)
        t.pencolor("white")
        koch_curve2(t, depth-1, size, w)
        t.lt(75)
        t.pencolor("green")
        koch_curve2(t, depth-1, size, w)
        
    
def tree(t, depth, size, angle):
    if depth == 0:
        t.fd(size)
        t.bk(size)
    else:
        t.fd(size)
        t.rt(angle)
        tree(t, depth-1, size, angle)
        t.lt(2 * angle)
        tree(t, depth-1, size, angle)
        t.rt(angle)
        t.bk(size)

def tree1(t, depth, size, angle, width):
    t.width(width)
    angle = angle * (random.randrange(8,12))/10
    if depth == 0:
        t.pencolor("green")
        t.fd(size)
        t.bk(size)
        t.pencolor("brown")
    else:
        t.pencolor("brown")
        t.fd(size)
        t.rt(angle)
        tree1(t, depth-1, size*0.8, angle, width*0.75)
        t.lt(2 * angle)
        tree1(t, depth-1, size*0.8, angle, width*0.75)
        t.rt(angle)
        t.bk(size)
        
def triangle(t, size):
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)

def triangle1(t, size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.lt(60)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(120)
    t.fd(size)
    t.rt(180)
    t.end_fill()
    
def sierpinski(t, depth, size, scale_factor=1):
    if depth == 1:
        triangle(t, size)
    else:
        sierpinski(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(60)
        t.fd(size/2)
        t.rt(60)
        sierpinski(t, depth-1, size/2)
        t.rt(120)
        t.fd(size/2)
        t.lt(120)

def sierpinski1(t, depth, size, scale_factor=1):
    if depth == 1:
        color = (random.randrange(255),random.randrange(255), random.randrange(255))
        triangle1(t, size, color)
    else:
        sierpinski1(t, depth-1, size/2)
        t.fd(size/2)
        sierpinski1(t, depth-1, size/2)
        t.bk(size/2)
        t.lt(60)
        t.fd(size/2)
        t.rt(60)
        sierpinski1(t, depth-1, size/2)
        t.rt(120)
        t.fd(size/2)
        t.lt(120)
        
        
raphael = turtle.Turtle()
#koch_curve(raphael, 4, 25)

#raphael.lt(90)
#tree1(raphael, 6, 45, 30, 5)
#tree(raphael, 5, 40, 30)

#sierpinski(raphael, 4, 200)
#sierpinski1(raphael, 4, 200)

raphael.pu()
raphael.goto(-600, 0)
raphael.pd()

#koch_curve2(raphael, 4, 15, 2)


window.exitonclick()
turtle.speed(0)
#  (t, 5, 200)

