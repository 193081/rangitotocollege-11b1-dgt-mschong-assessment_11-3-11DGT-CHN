from random import randint
from turtle import *
import time

def start_snek():

    delay = 0.1
    score = 0
    high_score = 0

    area = Screen()
    area.title("Snake with Turtle")
    area.bgcolor("black")
    area.setup(width=1000, height=800)
    area.tracer(0)

    frame = Turtle()
    frame.hideturtle()
    frame.color("white")   
    frame.penup()
    frame.goto(-410, -410)
    frame.pendown()
    for i in range(4):
        frame.forward(820)
        frame.left(90)


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
    pen.goto(0, 300)
    pen.write("Score: 0  High Score: 0", align="center", font=("Consolas", 18, "normal"))

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

    area.listen()
    area.onkeypress(go_up, "w")
    area.onkeypress(go_up, "Up")
    area.onkeypress(go_down, "s")
    area.onkeypress(go_down, "Down")
    area.onkeypress(go_left, "a")
    area.onkeypress(go_left, "Left")
    area.onkeypress(go_right, "d")
    area.onkeypress(go_right, "Right")


    while True:
        try:
            area.update()
        except Terminator:
            print("Snake game closed.")
            break
        if abs(head.xcor()) > 400 or abs(head.ycor()) > 400:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Consolas", 18, "normal"))

        if head.distance(food) < 20:
            x = randint(-20, 20) * 20
            y = randint(-20, 20) * 20
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
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Consolas", 18, "normal"))

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
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Consolas", 18, "normal"))

        time.sleep(delay)

if __name__ == "__main__":
    start_snek()