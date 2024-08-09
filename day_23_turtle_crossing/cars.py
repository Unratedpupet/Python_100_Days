from turtle import Turtle
import random

colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'orange', 'purple', 'pink', 'brown', 'gray', 'black', 'white', 'navy', 'maroon', 'lime', 'olive', 'teal', 'aqua', 'fuchsia']


class Car(Turtle):

    def __init__(self, shape: str = "square") -> None:
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(colors))
        self.move_speed = 5
        self.goto(x=random.randint(-300, 300), y=random.randint(-240, 290))


    def move(self):
        self.goto(self.xcor() - self.move_speed, self.ycor())
        if self.xcor() < -320:
            self.reset_position()

    def reset_position(self):
        self.goto(x=320, y=random.randint(-240, 290))
