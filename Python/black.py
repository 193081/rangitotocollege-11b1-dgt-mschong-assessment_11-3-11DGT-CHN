import random
from turtle import *
import time


def start_black():

    delay = 0.1
    score = 0
    high_score = 0

    wn = Screen()
    wn.title("Blackjack with Turtle")
    wn.bgcolor("green")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    frame = Turtle()
    frame.hideturtle()
    frame.color("white")   
    frame.penup()
    frame.goto(-410, -410)
    frame.pendown()
    for i in range(4):
        frame.forward(820)
        frame.left(90)

    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

    button = Turtle()
    button.hideturtle()
    button.speed(0)
    button.shape('circle')
