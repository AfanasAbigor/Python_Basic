import turtle as You_Know_Who
import random

tim = You_Know_Who.Turtle()
You_Know_Who.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)


screen = You_Know_Who.Screen()
screen.exitonclick()
