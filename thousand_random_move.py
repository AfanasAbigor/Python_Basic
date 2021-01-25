from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(9)

color = ["red", "green", "pink", "black", "IndianRed", "Blue", "LightSeaGreen", "orange", "SlateGrey","gold","lawngreen",
         "GreenYellow","LightSeaGreen"]
tim.speed("fastest")

directions = [0, 90, 180, 270]


for _ in range(1000):
    tim.color(random.choice(color))
    tim.forward(15)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
