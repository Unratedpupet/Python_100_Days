from turtle import Turtle

STARTING_HEADING = 40
BALL_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")

    def move(self):
        self.setheading(STARTING_HEADING)
        self.forward(BALL_SPEED)
