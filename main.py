from turtle import Turtle, Screen

timy = Turtle()
timy.shape("turtle")
timy.color(('cyan'), ('black'))
# timy.pencolor('#00FF7F')
# for _ in range(4):
#     timy.forward(100)
#     timy.right(90)


print(timy.pos())
lenght = 0
while lenght < 400:
    for colour in ("#00FF7F", "white"):
        timy.forward(10)
        timy.color(colour)
        lenght += 10

print(timy.pos())


screen = Screen()
screen.exitonclick()