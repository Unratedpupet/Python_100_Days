from turtle import Screen
import turtle as t
import random
# import colorgram


tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)



# def draw_square(perimeter_length: int):
#     """Draws a square without asking for starting position.

#     Args:
#         perimeter_length (int): The length of the perimeter square to draw.
#     """
#     for _ in range(4):
#         tim.forward(perimeter_length)
#         tim.right(90)

# # draw_square(100)

# def draw_dashed_line(length: int):
#     for _ in range(length):
#         tim.pd()
#         tim.forward(10)
#         tim.pu()
#         tim.forward(10)

# # draw_dashed_line(20)    

# def draw_shapes(sides: int):
#     tim.pencolor(random_color())
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)

# def draw_shapes_number(num_shapes: int):
#     """Draws a number of shapes depending on the amount inputted.

#     Args:
#         num_shapes (int): The number of shapes to be drawn.
#     """
#     # Makes sure that the shape is at least a triangle, so that it always draws shapes instead of a line.
#     for _ in range(3, num_shapes + 3):
#         draw_shapes(_)



# # draw_shapes_number(10)

# # Random walk - https://en.wikipedia.org/wiki/Random_walk

# tim.pensize(3)
# tim.speed(15)

# directions = [0, 90, 180, 270]

# def random_walk(steps: int):
#     for _ in range(steps):
#         tim.pencolor(random_color())
#         tim.forward(20)
#         tim.setheading(random.choice(directions))

# # random_walk(50)

# def draw_circles(num_circles: int, radius: int):

#     angle = 360 / num_circles  # Calculate the angle increment
#     count = 0

#     for _ in range(num_circles):
#         tim.pencolor(random_color())
#         tim.circle(radius)
#         tim.setheading(tim.heading() + angle)


# draw_circles(360, 100)

# Used to extract rgb colors from an image using colorgram.py

# color_grams = colorgram.extract("images/image.jpg", 20)
# # <colorgram.py Color: Rgb(r=252, g=250, b=247), 85.53812111915707%>
# # print(color_grams[0].rgb)
# colors = []
# for color in color_grams:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))

# Colors that were extracted using colorgram minus whites
color_list = [(213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111)]


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# 10 x 10 dots
# pensize 20
# 50 paces between

def hirst_painting(length: int, width: int, step_value: int):

    tim.penup()

    for i in range(length):
        
        for j in range(width):
            tim.setposition(j*step_value, i*step_value)
            tim.dot(20, random_color())
        
hirst_painting(20, 20, 20)


# Must remain at bottom
screen = Screen()
screen.exitonclick()