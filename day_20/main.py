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

is_alive = True

# Bind the key events outside the main loop
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.move_down, key='s')
screen.onkey(fun=snake.move_right, key='d')
screen.onkey(fun=snake.move_left, key='a')

while is_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()
        
screen.exitonclick()