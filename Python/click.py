from turtle import *

def click_check(x, y):
    print("Clicked at", x, y)

def click_start():
    score = 0
    increment = 1
    #You want to see inefficient coding? HERE YOU GO SUCKA.
    cost1 = 10 
    cost2 = 100
    counter = 2
    counter2 = 2

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
    upgrade.goto(250, -20)
    upgrade.write("Upgrades", align="center", font=("Consolas", 12, "normal"))
    upgrade.goto(250, -90)
    upgrade.write("+1", align="center", font=("Consolas", 20, "normal"))

    cost = Turtle()
    cost.hideturtle()
    cost.speed(0)
    cost.goto(250, -50)
    cost.write(f"Cost: {cost1}", align="center", font=("Consolas", 12, "normal"))

    def buttonfunc(x, y):
        nonlocal score, increment, cost1, counter
        if 200 <= x <= 300 and -100 <= y <= -50:
            if score >= cost1:
                score -= cost1
                increment += 1
                counter *= 1.5
                counter = int(counter)
                print(counter)
                cost1 += counter
                pen.clear()
                pen.write(f"Score: {score}", align="center", font=("Consolas", 18, "normal"))
                cost.clear()
                cost.write(f"Cost: {cost1}", align="center", font=("Consolas", 12, "normal"))
        if 350 <= x <= 650 and 250 <= y <= 350:
            if score >= cost2:
                    pass # Placeholder for second upgrade logic
        distance = (x**2 + y**2)**0.5
        if distance <= 50:
            score += increment
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Consolas", 18, "normal"))
            
    
    screen.onclick(buttonfunc)
    
    def quit_game():
        try:
            screen.bye()
        except:
            pass

    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", quit_game)

    screen.mainloop()

if __name__ == "__main__":
    click_start()