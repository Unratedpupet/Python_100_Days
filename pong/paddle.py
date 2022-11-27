from turtle import Turtle


UP = 90
DOWN = 270
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__("square")
        self.resizemode("user")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(starting_pos)
        self.setheading(UP)
        self.shapesize(1, 5, 1)

    def up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)

    def down(self):
        self.new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), self.new_y)
