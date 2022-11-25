from turtle import Turtle
import random

FOOD_SIZE = 0.3


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.turtlesize(FOOD_SIZE)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
