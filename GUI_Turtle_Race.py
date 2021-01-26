from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500) #Set height & width of Screen
screen.bgcolor("black") #change BackGround Color

line = Turtle("turtle")
line.goto(250, 250)
line.color("white")
line.right(90)
line.forward(500)


user_bet = screen.textinput(title="Make Your Bet From Rainbow Color!!!",
                            prompt="Which Turtle Will Win The Race? Enter A Color!").lower()

colors = ["purple", "blue", "skyblue", "green", "yellow", "orange", "red"]

list_y = [-70, -40, -10, 20, 50, 80, 110] #y coordinate distance

all_turtle = []

is_race_on = False

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=list_y[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230: #250-20 = size of turtle is 20 pixel.
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won!\n{winning_color} is The Winner!!!")
            else:
                print(f"You Have Loss.\nThe Winning Turtle is {winning_color}.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
