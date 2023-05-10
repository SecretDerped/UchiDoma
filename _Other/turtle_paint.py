from turtle import *

t = Turtle()
t.color('pink')
t.shape('circle')
t.pendown()


def draw(x, y):
    t.goto(x, y)


t.ondrag(draw)
