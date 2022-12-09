from turtle import Turtle
from random import randint


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color("red")
        self.goto(280, randint(200, 400))
        self.setheading(180)

    def move(self):
        self.forward(10)
