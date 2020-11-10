from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract("spot.jpg", 100)


rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


turtle = Turtle()
screen = Screen()
screen.screensize(740, 480)
screen.colormode(255)
turtle.speed("fastest")
turtle.penup()
turtle.setpos(-250, -250)
turtle.hideturtle()
y = -350
for x in range(10):
    for y in range(10):
        #turtle.pendown()
        color = random.choice(rgb_colors)
        turtle.pencolor(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        #turtle.penup()
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


























screen = Screen()
screen.exitonclick()
