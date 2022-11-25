from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
