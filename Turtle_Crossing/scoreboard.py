from turtle import  Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.upadate_scoreboard()

    def upadate_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increse_level(self):
        self.level += 1
        self.upadate_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", align="left", font=FONT)


