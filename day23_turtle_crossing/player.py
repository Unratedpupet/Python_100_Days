from turtle import Turtle

MOVE_AMOUNT = 10
STARTING_POS = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.color("black")
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_AMOUNT)

    def reset_position(self):
        self.goto(STARTING_POS)
