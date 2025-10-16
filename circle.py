from turtle import *
from colorsys import hsv_to_rgb

tracer(10)
bgcolor("black")
pensize(1)
h = 0.0

def draw(ang, n):
    circle(50 + n, 60)
    left(ang)
    circle(50 + n*2, 60)

up()
goto(0, 20)
down()

for i in range(200):
    color(hsv_to_rgb(h, 1, 1))
    h += 0.0062
    draw(90, 1)
    draw(180, 0)
    draw(0.5, 0)
    draw(120, 0)
    draw(0.5, 0)
    draw(120, 0)

hideturtle()
done()
