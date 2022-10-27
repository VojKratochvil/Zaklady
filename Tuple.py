# Nejde měnit vnitřní hodnoty


from turtle import Turtle, Screen
import random
import turtle

# Změna barevného módu
turtle.colormode(255)

tommy = Turtle()
tommy.shape("turtle")


def random_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     random_color = (r, g, b)
     return random_color


 # colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4", "blue4"]
rotation = [0, 90, 180, 270]
speed = 1

for number in range(200):
     # Náhodný výběr barvy
     tommy.pencolor(random_color())

     # Tloušťka čáry se zvyšuje
     if number <= 10:
         tommy.pensize(number)

     # Pohyb a náhodné otočení
     tommy.forward(30)
     tommy.right(random.choice(rotation))

     # Zvyšujeme rychlost
     tommy.speed(speed)
     speed += 1

my_screen = Screen()
my_screen.exitonclick()

