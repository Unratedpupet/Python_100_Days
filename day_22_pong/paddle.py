from turtle import Turtle

PADDLE_HEIGHT = 4

class Paddle(Turtle):

    
    def __init__(self, x_pos) -> None:
        super().__init__()
        self.y_increment = -20
        self.paddle_segments = []
        for _ in range(PADDLE_HEIGHT):
            new_paddle_segment = Turtle("square")
            new_paddle_segment.penup()
            new_paddle_segment.color("white")
            new_paddle_segment.goto(x_pos, self.y_increment)
            self.paddle_segments.append(new_paddle_segment)
            self.y_increment += 20
            

    def move_up(self):
        self.paddle_segments[0].goto(self.paddle_segments[0].xcor(), self.paddle_segments[0].ycor() + 10)