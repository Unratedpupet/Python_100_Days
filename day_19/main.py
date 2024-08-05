import turtle as t
import random

STARTING_X_POS = -220
STARTING_Y_POS = -60
FINISH_LINE = 230


colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []


screen = t.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

def race_prep():
    y_increment = 0
    for turtle_index in range(6):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.pu()
        new_turtle.setposition(STARTING_X_POS, STARTING_Y_POS + y_increment)
        y_increment += 30
        all_turtles.append(new_turtle)
    

def move_forward():
    pass

is_race_on = False

if user_bet:
    is_race_on = True

race_prep()

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= FINISH_LINE:
            is_race_on = False
            winner = turtle.pencolor().title()
            if user_bet == winner:
                print("You win!")
            else:
                print("You lost")
            print(f"The {turtle.pencolor().title()} turtle won the race!")
            


screen.exitonclick()
