from turtle import *

def click_check(x, y):
    print("Clicked at", x, y)

def click_start():
    score = 0
    increment = 1

    screen = Screen()
    screen.tracer(0)
    screen.title("Clicker Simulator")
    screen.bgcolor("lightblue")
    screen.setup(width=1000, height=800)

    pen = Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)
    pen.write(f"Score: {score}", align="center", font=("Consolas", 18, "normal"))

    button = Turtle()
    button.hideturtle()
    button.speed(0)
    button.color('black')
    button.fillcolor('red')
    button.penup()
    button.goto (0, -50)
    button.pendown()
    button.begin_fill()
    button.circle(50)
    button.end_fill()

    upgrade = Turtle()
    upgrade.width(3)
    upgrade.hideturtle()
    upgrade.speed(0)
    upgrade.color('black')
    upgrade.fillcolor('white')
    upgrade.penup()
    upgrade.goto (200, -50)
    upgrade.pendown()
    upgrade.begin_fill()
    for _ in range(2):
        upgrade.forward(100)
        upgrade.right(90)
        upgrade.forward(50)
        upgrade.right(90)
    upgrade.end_fill()
    upgrade.penup()
    upgrade.goto(250, -50)
    upgrade.pendown()
    upgrade.write("Cost: 10", align="center", font=("Consolas", 12, "normal"))
    upgrade.penup()
    upgrade.goto(250, -20)
    upgrade.write("Upgrades", align="center", font=("Consolas", 12, "normal"))

    def buttonfunc(x, y):
        nonlocal score
        distance = (x**2 + y**2)**0.5
        if distance <= 50:
            while False:
                print("Button clicked!")
            score += increment
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Consolas", 18, "normal"))
    
    screen.onclick(click_check)
    
    def quit_game():
        try:
            screen.bye()
        except:
            pass

    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", quit_game)

    screen.mainloop()

if __name__ == "__main__":
    click_start()