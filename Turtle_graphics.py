from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("blue")

# Kreslení čtverce
# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# nebo

# for x in range(0, 4):
#     tommy.forward(100)
#     tommy.right(90)

# kreslení obrazce
moves = 3
while moves !=9:
    for x in range(moves):
        tommy.forward(100)
        tommy.right(360/moves)
    moves += 1


my_screen = Screen()
# print(f"šířka: {my_screen.canvwidth}")
# print(f"výška: {my_screen.canvheight}")
my_screen.exitonclick()
