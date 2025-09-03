from random import randint
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
    head.shape('square')
    head.color('green')
    head.direction = 'stop'
    head.penup()
    head.goto(0, 0)
    
    food = Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

    def go_up():
        if head.direction != "down":
            head.direction = "up"
    def go_down():
        if head.direction != "up":
            head.direction = "down"
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    def go_right():
        if head.direction != "left":
            head.direction = "right"
    def move():
        if head.direction == "up":
            head.sety(head.ycor() + 20)
        if head.direction == "down":
            head.sety(head.ycor() - 20)
        if head.direction == "left":
            head.setx(head.xcor() - 20)
        if head.direction == "right":
            head.setx(head.xcor() + 20)

    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_up, "Up")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_down, "Down")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_left, "Left")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_right, "Right")


    while True:
        wn.update()

        if abs(head.xcor()) > 300 or abs(head.ycor()) > 300:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        if head.distance(food) < 20:
            x = randint(-14, 14) * 20
            y = randint(-14, 14) * 20
            food.goto(x, y)
            new_segment = Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)
            delay = max(0.05, delay - 0.001)
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        for i in range(len(segments)-1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)
        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())
            
        move()

        for seg in segments:
            if seg.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                for seg in segments:
                    seg.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

        time.sleep(delay)

if __name__ == "__menu__":
    start_snek()