from turtle import Turtle
import random

MOVE_SPEED = 15
TOP = 320
BOTTOM = -320
RIGHT = 300
LEFT = -300

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(45)

    def move(self):
        
        self.forward(MOVE_SPEED)
        # self.bounce_sides()
        self.bounce_top_bottom()

    def bounce_top_bottom(self):
        if self.ycor() >= TOP: 
            self.setheading(self.heading() - 90)
        elif self.ycor() <= BOTTOM:
            self.setheading(self.heading() + 90)
        
    def bounce_sides(self):
        print(self.xcor())
        if self.xcor() >= RIGHT or self.xcor() <= LEFT:
            self.setheading(self.heading() +180)

