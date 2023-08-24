import turtle as t
import random as r
from turtle import Turtle, Screen

t.colormode(255)

rgb_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17),
            (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24),
            (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162)]

tom = Turtle()
tom.shape("circle")
tom.speed('fastest')
tom.hideturtle()

def start_point():
    tom.setheading(225)
    tom.penup()
    tom.forward(300)
    tom.setheading(0)


def left_mvmt():
    tom.left(90)
    tom.forward(40)
    tom.left(90)


def right_mvmt():
    tom.right(90)
    tom.forward(40)
    tom.right(90)


start_point()
for i in range(10):
    for j in range(10):
        tom.dot(20, r.choice(rgb_list))
        tom.penup()
        tom.forward(40)
    if i % 2 == 0:
        left_mvmt()
    else:
        right_mvmt()


screen = Screen()
screen.exitonclick()