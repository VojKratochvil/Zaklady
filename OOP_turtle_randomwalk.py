from turtle import Turtle, Screen
import random


tommy = Turtle()
tommy.shape("turtle")

color = ["red", "green", "blue", "black", "pink"]
random_colour = random.choice(color)

tommy.color(random_colour)

number= 1

for x in range(100):
    angle = random.randrange(0, 360)
    tommy.forward(100)
    tommy.right(angle)
    tommy.speed(number)
    number += 1
    if number == 10:
        number -= 1
    tommy.pensize(number)




my_screen = Screen()

my_screen.exitonclick()
