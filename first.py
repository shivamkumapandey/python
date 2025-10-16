import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.speed(10)
flower.pencolor("purple")

# Function to draw a single petal
def draw_petal():
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Draw all petals
for _ in range(6):
    flower.begin_fill()
    flower.color("violet")
    draw_petal()
    flower.end_fill()
    flower.left(60)

# Draw the flower's center
flower.penup()
flower.goto(0, -40)
flower.pendown()
flower.begin_fill()
flower.color("yellow")
flower.circle(40)
flower.end_fill()

# Hide the turtle and finish
flower.hideturtle()
screen.exitonclick()
