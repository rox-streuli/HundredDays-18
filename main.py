import turtle
from turtle import Turtle, Screen
from colour_list import colour
from random import choice, randint

#
# def next_move():
#     return choice([True, False])
#
#
# def turn():
#     if next_move():
#         timy.left(90)
#     else:
#         timy.right(90)
#
#
# def advance():
#     if next_move():
#         timy.forward(20)
#     else:
#         timy.backward(20)


timy = Turtle()
# to generate a random rgb colour first change the turtle colormode()
# method. Then create a function to generate random rgb colour tuples.
# use it with timy.pencolor(tuple)
turtle.colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


# # hid timy from view
# timy.hideturtle()
# # do not draw a line qhile moving
# timy.penup()
# # move timy to new position
# timy.goto(-100, 300)
# # reveal timy new position
# timy.showturtle()
# # allow timy to write again
# timy.pendown()

# give timy new shape
timy.shape("turtle")
# set timy new colours
# timy.color(('cyan'), ('black'))
# timy.pencolor('#00FF7F')
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
#
# for sides in range(3, 11):
#     timy.color(choice(colour))
#     for _ in range(sides):
#         angle = 360 / sides
#         timy.forward(100)
#         timy.right(angle)

# make timy do a random walk
# make timy fast!
timy.speed(0)
# make timy draw a thick line
# timy.pensize(6)
# #
# for _ in range(400):
#     # timy.color(choice(colour))
#     timy.pencolor(random_colour())
#     advance()
#     turn()


# her solution was to use .setheading()
# easier than my solution
# for _ in range(400):
    # timy.color(choice(colour))
    # timy.forward(30)
    # timy.setheading(choice([0,90,180, 270]))


# make timy draw a spirograph with random colours
# for _ in range (0, 360, 3):
#     timy.pencolor(random_colour())
#     timy.circle(100)
#     timy.setheading(_)

# you can create a function and set gap between circles
def spirograph(gap):
    for _ in range(0, 360, gap):
        timy.pencolor(random_colour())
        timy.circle(100)
        timy.setheading(_)


spirograph(10)  # XD

screen = Screen()
screen.exitonclick()