import turtle as t
from ball import Ball
import time
from paddle import Paddle

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200
RIGHT_PADDLE_X_POS = 550
LEFT_PADDLE_X_POS = -550

ball = Ball()
right_paddle = Paddle(RIGHT_PADDLE_X_POS)
left_paddle = Paddle(LEFT_PADDLE_X_POS)





screen = t.Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.tracer(0)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    ball.move() 
    right_paddle.move_up()




screen.exitonclick()