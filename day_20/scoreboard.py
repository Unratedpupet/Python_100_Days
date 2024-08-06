from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 280)
        self.write_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.setposition(0, 0)
        self.write(f"GAME OVER. Your score was: {self.score}", align=ALIGNMENT, font=FONT)
        