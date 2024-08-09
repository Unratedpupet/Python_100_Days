from turtle import Turtle

MOVE_SPEED = 10


class Player(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("brown")
        self.shape("turtle")
        self.setheading(90)
        self.start_position()

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_SPEED)

    def start_position(self):
        self.goto(0, -280)