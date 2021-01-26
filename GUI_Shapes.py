from turtle import Turtle, Screen
import random

timm = Turtle()
timm.shape("arrow")

colours = ["red", "green", "red", "black", "IndianRed", "Blue", "LightSeaGreen", "orange", "SlateGrey"]

for i in range(3, 11):

    timm.color(random.choice(colours))
    num_sides = i
    for _ in range(num_sides):
        angle = 360 / num_sides
        timm.forward(100)
        timm.right(angle)
    num_sides = 0


screen = Screen()
screen.exitonclick()
