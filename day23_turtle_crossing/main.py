from turtle import Screen
from player import Player
from car import Car
import time


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Turtle Crossing")
screen.tracer(0)


player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True

car = Car()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    if player.ycor() > 290:
        player.reset_position()


    car.move()

screen.exitonclick()
