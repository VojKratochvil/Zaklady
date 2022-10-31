from turtle import Turtle, Screen
import random
import turtle

# Změna barvy
turtle.colormode(255)

# Nastavení objektu
tommy = Turtle()
tommy.shape("turtle")
tommy.speed(20)

# nahodna barva
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# number_of_circles = 90
#
# for x in range(number_of_circles):
#     tommy.pencolor(random_color())
#     tommy.circle(90)
#     tommy.left(360/number_of_circles)

# nebo
def spirograf(number):
    for x in range(number):
        tommy.pencolor(random_color())
        tommy.circle(90)
        tommy.left(360 / number)

spirograf(80)

my_screen = Screen()
my_screen.exitonclick()
