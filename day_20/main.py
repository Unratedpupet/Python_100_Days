import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake SSSSSSSSSSSSssss")
screen.tracer(0)
screen.listen()

snake = Snake()

# x_increment = 0
# for _ in range(3):

#     new_snake = t.Turtle(shape="square")
#     new_snake.color("white")
#     new_snake.pu()
#     new_snake.setposition(x=x_increment, y=0)
#     snake_body.append(new_snake)
#     x_increment -= 20


# def move_up():
#     snake_body[0].setheading(90)
    

# def move_down():
#     snake_body[0].setheading(270)
    

# def move_right():
#     snake_body[0].setheading(0)
    

# def move_left():
#     snake_body[0].setheading(180)
    

# screen.onkey(fun=move_up, key='w')
# screen.onkey(fun=move_down, key='s')
# screen.onkey(fun=move_right, key='d')
# screen.onkey(fun=move_left, key='a')


is_alive = True

while is_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()
        
        





screen.exitonclick()