import turtle as t

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x_increment = 0
        for _ in range(3):
            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()  # Use 'penup' instead of 'pu' for clarity
            new_snake.setposition(x=x_increment, y=0)
            self.snake_body.append(new_snake)
            x_increment -= 20

    def add_body(self):
            new_snake = t.Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()  # Use 'penup' instead of 'pu' for clarity
            new_snake.setposition(self.snake_body[-1].position())
            self.snake_body.append(new_snake)

    def move_up(self):
        if self.head.heading() != DOWN:  # Prevent moving directly backward
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:  # Prevent moving directly backward
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:  # Prevent moving directly backward
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:  # Prevent moving directly backward
            self.head.setheading(LEFT)

    def move(self):
        for snake_body_index in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake_body_index-1].xcor()
            new_y = self.snake_body[snake_body_index-1].ycor()
            self.snake_body[snake_body_index].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def detect_wall_collision(self) -> bool:

        if self.head.xcor() >= 300 or self.head.xcor() <= -300 or self.head.ycor() >= 300 or self.head.ycor() <= -300:
            print("Game Over")
            return False
        else:
            return True
        
    def detect_tail_collision(self) -> bool:
        for segment in self.snake_body[1:]:
            return not self.head.distance(segment) < 10
                
    
    
