"""A simple clicker game.

Click the big red button to earn points.
Use points to buy upgrades.
Get to one million points to win!
"""

from turtle import Turtle, Screen


def click_start():
    """Start the clicker game."""
    score = 0
    increment = 1
    timerinc = 0
    cost1 = 10
    cost2 = 100
    counter = 2
    counter2 = 2

    #Main screen setup
    screen = Screen()
    screen.tracer(0)
    screen.title("Clicker Simulator")
    screen.bgcolor("lightblue")
    screen.setup(width=1000, height=800)
    screentk = screen.getcanvas().winfo_toplevel()
    screentk.attributes('-fullscreen', True)
    screen.onkey(screen.bye, "Escape")
    screen.listen()

    goal = Turtle()
    goal.hideturtle()
    goal.penup()
    goal.goto(0, 250)
    goal.write("Goal: Reach 10,000 points!", align="center",
               font=("Arial", 24, "bold"))

    pen = Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)
    pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    # The button
    button = Turtle()
    button.hideturtle()
    button.speed(0)
    button.color('black')
    button.fillcolor('red')
    button.penup()
    button.goto(0, -100)
    button.pendown()
    button.begin_fill()
    button.circle(100)
    button.end_fill()
    button.penup()
    button.goto(0, -20)
    button.write("CLICK ME", align="center", font=("Arial", 25, "bold"))

    # Upgrade buttons
    upgrade = Turtle()
    upgrade.width(3)
    upgrade.hideturtle()
    upgrade.speed(0)
    upgrade.color('black')
    upgrade.fillcolor('white')
    upgrade.penup()
    upgrade.goto(200, -50)
    upgrade.pendown()
    upgrade.begin_fill()
    for i in range(2):
        upgrade.forward(100)
        upgrade.right(90)
        upgrade.forward(50)
        upgrade.right(90)
    upgrade.end_fill()
    upgrade.penup()
    upgrade.goto(250, -20)
    upgrade.write("Upgrades", align="center", font=("Arial", 12, "bold"))
    upgrade.goto(250, -90)
    upgrade.write("+1", align="center", font=("Arial", 20, "bold"))
    upgrade.goto(200, -120)
    upgrade.pendown()
    upgrade.begin_fill()
    for i in range(2):
        upgrade.forward(100)
        upgrade.right(90)
        upgrade.forward(50)
        upgrade.right(90)
    upgrade.end_fill()
    upgrade.penup()
    upgrade.goto(250, -160)
    upgrade.write("+1/s", align="center", font=("Arial", 20, "bold"))

    cost = Turtle()
    cost.hideturtle()
    cost.speed(0)
    cost.goto(250, -50)
    cost.write(f"Cost: {cost1}", align="center", font=("Arial", 12, "normal"))
    cost.goto(250, -120)
    cost.write(f"Cost: {cost2}", align="center", font=("Arial", 12, "normal"))

    # Quitting stuff.
    quit = Turtle()
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

    def quit_game(x, y):
        if -550 <= x <= -450 and 370 <= y <= 410:
            screen.bye()

    def timerfunc(milliseconds):
        nonlocal timerinc
        if timerinc >= 1:
            time = int(milliseconds / timerinc)
            return time
        else:
            return milliseconds

    def add_points():
        nonlocal score, timerinc, cost2
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center",
                  font=("Arial", 24, "bold"))
        screen.ontimer(lambda: add_points(), timerfunc(1000))

    # The button operation.
    def buttonfunc(x, y):
        nonlocal score, increment, cost1, counter, counter2, cost2, timerinc
        quit_game(x, y)
        if 200 <= x <= 300 and -100 <= y <= -50:
            if score >= cost1:
                score -= cost1
                increment += 1
                counter *= 1.5
                counter = int(counter)
                cost1 += counter
                pen.clear()
                pen.write(f"Score: {score}", align="center",
                          font=("Arial", 24, "bold"))
                cost.clear()
                cost.goto(250, -50)
                cost.write(f"Cost: {cost1}", align="center",
                           font=("Arial", 12, "normal"))
                cost.goto(250, -120)
                cost.write(f"Cost: {cost2}", align="center",
                           font=("Arial", 12, "normal"))
        if 200 <= x <= 300 and -170 <= y <= -120:
            if score >= cost2:
                score -= cost2
                timerinc += 1
                counter2 *= 1.5
                counter2 = int(counter2)
                add_points()
                print(counter2)
                cost2 += counter2
                pen.clear()
                pen.write(f"Score: {score}", align="center",
                          font=("Arial", 24, "bold"))
                cost.clear()
                cost.goto(250, -50)
                cost.write(f"Cost: {cost1}", align="center",
                           font=("Arial", 12, "normal"))
                cost.goto(250, -120)
                cost.write(f"Cost: {cost2}", align="center",
                           font=("Arial", 12, "normal"))
        distance = (x**2 + y**2)**0.5
        if distance <= 100:
            score += increment
            pen.clear()
            pen.write(f"Score: {score}", align="center",
                      font=("Arial", 24, "bold"))
        if score >= 10000:
            screen.clear()
            screen.bgcolor("gold")
            pen.color("black")
            pen.goto(0, 0)
            pen.write("You win!", align="center",
                      font=("Comic Sans MS", 36, "bold"))
            pen.goto(0, -50)
            pen.write("Press 'Esc' to quit", align="center",
                      font=("Comic Sans MS", 24, "normal"))
            screen.onkey(screen.bye, "Escape")

    screen.onclick(buttonfunc)

    screentk.protocol("WM_DELETE_WINDOW", screen.bye)

    screen.mainloop()

# Start the game if this file is run directly
if __name__ == "__main__":
    click_start()
