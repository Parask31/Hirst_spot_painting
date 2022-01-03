from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
tim.speed(15)

screen.colormode(255)

colour_list = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89), (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97), (222, 177, 182), (109, 128, 151)]

# Moving to starting location of painting.
tim.penup()
tim.goto(-200, -200)


def row():
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colour_list))
        tim.penup()
        tim.forward(50)


for _ in range(10):
    starting_location_x = tim.xcor()
    starting_location_y = tim.ycor()
    row()
    tim.goto(starting_location_x, starting_location_y+50)

screen.exitonclick()
