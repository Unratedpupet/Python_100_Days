from turtle import Turtle

PLAYER_STARTING_POSITION = (-350, 0)
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self):
        super().__init__("square")
        self.resizemode("user")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(PLAYER_STARTING_POSITION)
        self.setheading(UP)
        self.shapesize(1, 5, 1)

    def up(self):
        self.setheading(UP)
        self.forward(10)

    def down(self):
        self.setheading(DOWN)
        self.forward(10)
