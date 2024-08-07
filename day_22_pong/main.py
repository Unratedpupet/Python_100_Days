import turtle as t
from ball import Ball
import time

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1200

ball = Ball()





screen = t.Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.tracer(0)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move() 




screen.exitonclick()