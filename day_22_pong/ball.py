from turtle import Turtle
import random

MOVE_SPEED = 15
TOP = 320
BOTTOM = -320
RIGHT = 570
LEFT = -570

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.dx = MOVE_SPEED # Uses the move speed attribute to create the new position, instead of using headings. 
        self.dy = MOVE_SPEED # This will also prevent the ball from going on it's side making a diamond.

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy

        self.goto(new_x, new_y)

        self.bounce_sides()
        self.bounce_top_bottom()

    def bounce_top_bottom(self):
        if self.ycor() >= TOP or self.ycor() <= BOTTOM:
            self.dy *= -1

    def bounce_sides(self):
        if self.xcor() >= RIGHT or self.xcor() <= LEFT:
            self.dx *= -1