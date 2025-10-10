from turtle import *

def click_check(x, y):
    print("Clicked at", x, y)

def click_start():
    screen = Screen()
    screen.title("Clicker Simulator")
    screen.bgcolor("lightblue")
    screen.setup(width=1000, height=800)

    button = Turtle()
    button.hideturtle()
    button.speed(0)
    button.color('black')
    button.fillcolor('red')
    button.penup()
    button.goto (0, -25)
    button.circle(50)
    button.write("Click Me!", align="center", font=("Arial", 16, "bold"))
    button.pendown()
    button.begin_fill()
    button.circle(50)
    button.end_fill()

    
    while True:
        screen.onclick(click_check)
        break

    def quit_game():
        try:
            screen.bye()
        except:
            pass

    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", quit_game)

    screen.mainloop()

if __name__ == "__main__":
    click_start()