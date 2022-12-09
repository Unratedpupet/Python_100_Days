from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

WIDTH = 800
HEIGHT = 600
RIGHT_PADDLE_POSITION = (350, 0)
LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_SCORE_POSITION = (100, 250)
LEFT_SCORE_POSITION = (-100, 250)


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_POSITION)
l_paddle = Paddle(LEFT_PADDLE_POSITION)

right_score = Scoreboard(RIGHT_SCORE_POSITION)
left_score = Scoreboard(LEFT_SCORE_POSITION)

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


ball = Ball()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # Detects collision with top and bottom
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detects collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detects scoring
    if ball.xcor() > 400:
        # Left score point
        left_score.increase_score()
        ball.reset_position()
    elif ball.xcor() < -400:
        # Right score point
        right_score.increase_score()
        ball.reset_position()

screen.exitonclick()
