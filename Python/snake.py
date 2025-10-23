"""This is a simple snake game made with turtle.

control using WASD or arrow keys to move around the snake.
"""
from random import randint
from turtle import Screen, Turtle
import time


def start_snek():
    """Start the snek game."""
    delay = 0.1
    score = 0
    high_score = 0

    area = Screen()
    area.title("Snake with Turtle")
    area.bgcolor("#000000")
    area.setup(width=900, height=900)
    area.tracer(0)

    areatk = area.getcanvas().winfo_toplevel()
    areatk.attributes("-fullscreen", True)

    quit = Turtle()  # The quit button
    quit.hideturtle()
    quit.color("red")
    quit.fillcolor("red")
    quit.penup()
    quit.goto(-500, 450)
    quit.write("Press 'Esc' to Quit", align="center",
               font=("Arial", 15, "normal"))
    quit.goto(-500, 430)
    quit.write("(Progress is not saved)", align="center",
               font=("Arial", 10, "normal"))
    quit.goto(-550, 410)
    quit.pendown()
    quit.begin_fill()
    for _ in range(2):
        quit.forward(100)
        quit.right(90)
        quit.forward(40)
        quit.right(90)
    quit.end_fill()
    quit.penup()
    quit.goto(-500, 380)
    quit.color("black")
    quit.write("Quit", align="center", font=("Arial", 12, "bold"))

    area.onkey(area.bye, "Escape")

    # Turtles for the game.
    instructions = Turtle()
    instructions.hideturtle()
    instructions.penup()
    instructions.goto(0, 410)
    instructions.color("white")
    instructions.write("Use WASD or Arrow Keys to Move", align="center",
                       font=("Arial", 15, "normal"))

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
    head.color("#789716")
    head.direction = 'stop'
    head.penup()
    head.goto(0, 0)

    food = Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("#D62D2D")
    food.penup()
    food.goto(0, 100)

    segments = []

    pen = Turtle()
    pen.speed(0)
    pen.color("yellow")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 450)
    pen.write("Score: 0  High Score: 0", align="center",
              font=("Arial", 18, "normal"))
    
    # Movement functions
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

    def quit_game(x, y):
        if -550 <= x <= -450 and 370 <= y <= 410:
            area.bye()

    # The game loop and collision check.
    def gameloop():
        nonlocal delay, score, high_score
        area.update()

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
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Arial", 18, "normal"))

        if head.distance(food) < 20:
            x = randint(-20, 20) * 20
            y = randint(-20, 20) * 20
            food.goto(x, y)
            new_segment = Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#a5cb38")
            new_segment.penup()
            segments.append(new_segment)
            delay = max(0.05, delay - 0.001)
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}",
                      align="center", font=("Arial", 18, "normal"))

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
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}",
                          align="center", font=("Arial", 18, "normal"))
        area.ontimer(gameloop, int(delay * 1000))
# End of game loop and collision check.
# Set up the window close protocol
    areatk.protocol("WM_DELETE_WINDOW", area.bye)

    area.onclick(quit_game)

    gameloop()
    area.mainloop()

# Start the game if this file is run directly
if __name__ == "__main__":
    start_snek()
