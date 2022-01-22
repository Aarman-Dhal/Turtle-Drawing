import turtle 
import random 
from turtle import *

window = turtle.Screen()
screen = window.setup(1000, 1000)
window.title('Turtle Graphics')
window.bgcolor("white")

colors = ["red", "yellow", "green", "blue", "purple", "orange", "black"]
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

brush = turtle.Turtle()
brush.speed(0)
brush.pensize(5)


def right():
    brush.setheading(0)
    brush.forward(100)

def up():
    brush.setheading(90)
    brush.forward(100)

def left():
    brush.setheading(180)
    brush.forward(100)

def down():
    brush.setheading(270)
    brush.forward(100)

def clickLeft(x, y):
    brush.color(random.choice(colors))

def clickRight(x, y):
    brush.clear()

def draw_circle():
    brush.begin_fill()
    brush.circle(50)
    
def lift_pen():
    brush.penup()

def drop_pen():
    brush.down()

def stamp():
    brush.stamp()

def change_shape():
    brush.shape(random.choice(shapes)) 
    
turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 2)

turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(draw_circle, '1')
turtle.onkey(lift_pen, '2')
turtle.onkey(drop_pen, '3')
turtle.onkey(stamp, '4')
turtle.onkey(change_shape, '5')

turtle.mainloop()