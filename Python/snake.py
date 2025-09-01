from random import *
from turtle import *
import time

def start_snek():

    delay = 0.1
    score = 0
    high_score = 0

    wn = Screen()
    wn.title("Snake with Turtle")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    head = Turtle()
    head.speed(0)
    head.shape('Square')
    head.color('green')
    

    while True:
        wn.update()