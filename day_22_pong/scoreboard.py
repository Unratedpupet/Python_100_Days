from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self, player_num: int) -> None:
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.score = 0
        if player_num == 1:
            self.goto(-100, 280)
        else:
            self.goto(100, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # print("SCOREBOARD: Updating score")
        self.update_scoreboard()
