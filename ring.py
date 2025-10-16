from turtle import*
from colorsys import hsv_to_rgb 
import time

speed(0)
bgcolor("black")
h=0

screen = Screen()
screen.tracer(0)
for i in range(360):
    rgb = hsv_to_rgb(h, 1, 1)
    pencolor(rgb)
    h +=0.0025
    left(1)
    forward(2)
    for j in range(2):
        left(2)
        circle(80)
        screen.update()
        time.sleep(0.01)

hideturtle()
done()