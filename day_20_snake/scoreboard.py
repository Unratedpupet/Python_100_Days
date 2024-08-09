from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

with open("high_score.txt", 'r') as high_score_file:
    high_score = int(high_score_file.read())  # Convert to integer


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt", 'w') as high_score_file:
            high_score_file.write(str(self.high_score))  # Convert to string before writing
