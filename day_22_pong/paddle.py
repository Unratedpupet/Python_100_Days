from turtle import Turtle

PADDLE_HEIGHT = 5
PADDLE_SPEED = 15

class Paddle(Turtle):

    
    def __init__(self, x_pos) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
            

    def move_up(self):
        for paddle_index in range(len(self.paddle_segments)):
            self.paddle_segments[paddle_index].goto(self.paddle_segments[paddle_index].xcor(), self.paddle_segments[paddle_index].ycor() + PADDLE_SPEED)

    def move_down(self):
        for paddle_index in range(len(self.paddle_segments)):
            self.paddle_segments[paddle_index].goto(self.paddle_segments[paddle_index].xcor(), self.paddle_segments[paddle_index].ycor() - PADDLE_SPEED)