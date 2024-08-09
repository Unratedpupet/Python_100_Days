from turtle import Turtle

PADDLE_SPEED = 15

class Paddle(Turtle):

    
    def __init__(self, x_pos) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, 0)
            

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)