import turtle as t

class Snake:

    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        x_increment = 0
        for _ in range(3):
            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()  # Use 'penup' instead of 'pu' for clarity
            new_snake.setposition(x=x_increment, y=0)
            self.snake_body.append(new_snake)
            x_increment -= 20

    def move_up(self):
        if self.snake_body[0].heading() != 270:  # Prevent moving directly backward
            self.snake_body[0].setheading(90)

    def move_down(self):
        if self.snake_body[0].heading() != 90:  # Prevent moving directly backward
            self.snake_body[0].setheading(270)

    def move_right(self):
        if self.snake_body[0].heading() != 180:  # Prevent moving directly backward
            self.snake_body[0].setheading(0)

    def move_left(self):
        if self.snake_body[0].heading() != 0:  # Prevent moving directly backward
            self.snake_body[0].setheading(180)

    def move(self):
        for snake_body_index in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake_body_index-1].xcor()
            new_y = self.snake_body[snake_body_index-1].ycor()
            self.snake_body[snake_body_index].goto(new_x, new_y)
        
        self.snake_body[0].forward(20)