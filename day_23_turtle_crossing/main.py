from turtle import Turtle, Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

for _ in range(5):
    new_car = Car()
    cars.append(new_car)

screen.listen()
screen.onkeypress(dana.move_up, "w")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    
    for car in cars:
        car.move()

    if dana.ycor() > 290:
        dana.start_position()
        print("Next level!")
        scoreboard.increase_level()
        for car in cars:
            car.increase_speed()
        
    for car in cars:
        if dana.distance(car) < 20:
            print("Game Over")
            is_game_on = False

screen.exitonclick()