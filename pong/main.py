from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")

paddle = Paddle()

screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

scoreboard = Scoreboard()



screen.exitonclick()
