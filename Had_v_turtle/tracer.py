from turtle import Turtle, Screen
import time
import random

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
# tělo
body_parts = []

# Jídlo pro hada
food = Turtle("circle")
food.color("red")
food.penup()
x_start = random.randint(-screen_width / 2 + 20, screen_width / 2 + 20)
y_start = random.randint(-screen_height / 2 + 20, screen_height / 2 + 20)
food.goto(x_start, y_start)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Fuknce : připnout k Events.py
def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"

def move_left():
    head.direction = "left"

def move_right():
    head.direction = "right"


screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# Pohyb plynulý a hlavní cyklus
while True:
    screen.update()



    move()
    if head.distance(food) < 20:
        x = random.randint(-screen_width/2 + 20, screen_width/2 + 20)
        y = random.randint(-screen_height/2 + 20, screen_height/2 + 20)
        food.goto(x, y)

        # Hadí tělo
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for index in range(len(body_parts) -1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()
    time.sleep(0.15)



# for _ in range(80):
#     square1.forward(10)
#     square2.forward(10)
#     time.sleep(0.1)
#     screen.update()

screen.exitonclick()
