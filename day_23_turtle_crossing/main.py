from turtle import Turtle, Screen
from player import Player
from cars import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
"""
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.

"""

dana = Player()
cars = []

for _ in range(25):
    new_car = Car()
    cars.append(new_car)

screen.listen()
screen.onkey(dana.move_up, "w")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    
    for car in cars:
        car.move()


screen.exitonclick()