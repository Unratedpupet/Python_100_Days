import turtle as t
class Snake:

    def __init__(self) -> None:
        
        self.snake_body = []

        x_increment = 0
        for _ in range(3):

            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.pu()
            new_snake.setposition(x=x_increment, y=0)
            self.snake_body.append(new_snake)
            x_increment -= 20

    # def move_up(self):
    #     self.snake_body[0].setheading(90)
        

    # def move_down(self):
    #     self.snake_body[0].setheading(270)
        

    # def move_right(self):
    #     self.snake_body[0].setheading(0)
        

    # def move_left(self):
    #     self.snake_body[0].setheading(180)

    def move(self):
        for snake_body_index in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[snake_body_index].setposition(self.snake_body[snake_body_index-1].pos())
        
        self.snake_body[0].forward(10)
    