from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

WIDTH = 800
HEIGHT = 600
PLAYER_STARTING_POSITION = (350, 0)
COMP_STARTING_POSITION = (-350, 0)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(PLAYER_STARTING_POSITION)
l_paddle = Paddle(COMP_STARTING_POSITION)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

scoreboard = Scoreboard()
ball = Ball()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    ball.move()

screen.exitonclick()
