from turtle import *

def click_check(x, y):
    print("Clicked at", x, y)

def click_start():
    score = 0

    screen = Screen()
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

    def buttonfunc(x, y):
        nonlocal score
        distance = (x**2 + (y-50)**2)**0.5
        if distance <= 50:
            print("Button clicked!")
            score += 1
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