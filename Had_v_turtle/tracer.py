from turtle import Turtle, Screen
import time


screen_width = 800
screen_height = 800

screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v Hadí hře")
screen.setup(width=screen_width, height=screen_height)
screen.tracer(False)

# Hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

while True:
    move()
    time.sleep(0.1)
    screen.update()


# for _ in range(80):
#     square1.forward(10)
#     square2.forward(10)
#     time.sleep(0.1)
#     screen.update()

screen.exitonclick()
