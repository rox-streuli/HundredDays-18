from turtle import Turtle, Screen
from colour_list import colour
from random import choice

timy = Turtle()
# hid timy from view
timy.hideturtle()
# do not draw a line qhile moving
timy.penup()
# move timy to new position
timy.goto(-100, 300)
# reveal timy new position
timy.showturtle()
# allow timy to write again
timy.pendown()

# give timy new shape
timy.shape("turtle")
# set timy new colours
timy.color(('cyan'), ('black'))
timy.pencolor('#00FF7F')
# draw a square
# for _ in range(4):
#     timy.forward(100)
#     timy.right(90)

# test position
# print(timy.pos())

# # set control variable
# lenght = 0
# # set loop to draw dashed line
# while lenght < 400:
#     for colour in ("#00FF7F", "white"):
#         timy.forward(10)
#         timy.color(colour)
#         lenght += 10

# print(timy.pos())

# you can use this one too:
# for _ in range(15):
#     timy.forward(10)
#     timy.penup()
#     timy.forward(10)
#     timy.pendown()

# make timy draw a triangle, square, pentagon, hexagon, heptagon,
# octagon, nonagon and decagon, one in top of another

for sides in range(3, 11):
    timy.color(choice(colour))
    for _ in range(sides):
        angle = 360 / sides
        timy.forward(100)
        timy.right(angle)

screen = Screen()
screen.exitonclick()