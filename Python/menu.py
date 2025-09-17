from tkinter import *
import subprocess
import sys
from random import randint

def toggle_fullscreen(window):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def default_color(item):
    item.configure(bg='black', fg='white', font=('Arial', 10) )

def run_game(script_name):
    subprocess.Popen([sys.executable, script_name])

def random_game(window):
    i = randint(0,3)
    if i == 0:
        run_game("Python/snake.py")
    elif i == 1:
        run_game("Python/black.py")
    elif i == 2:
        run_game("Python/tet.py")
    elif i == 3:
        window.quit()

mainscreen = Tk()
mainscreen.title('Just another game compendium')
mainscreen.configure(bg='black')
mainscreen.geometry("800x600")

title_label = Label(mainscreen, text='Game Compendium', bg='black', fg='white', font=('Arial', 24, 'bold'))
title_label.pack(pady=20)

fullscreen = Button(mainscreen, text ='Fullscreen', width = 25, height = 10, command = lambda: toggle_fullscreen(mainscreen))
fullscreen.place(relx=0.75, rely=0.66, anchor='center')

snake_but = Button(mainscreen, text ='Snake', width = 25, height = 10, command = lambda: run_game("Python/snake.py"))
snake_but.place(relx=0.25, rely=0.33, anchor='center')

black_but = Button(mainscreen, text ='Blackjack', width = 25, height = 10, command = lambda: run_game("Python/black.py"))
black_but.place(relx=0.25, rely=0.66, anchor='center')

tet_but = Button(mainscreen, text = 'Tetris', width = 25, height = 10, command = lambda: run_game("Python/tet.py"))
tet_but.place(relx=0.75, rely=0.33, anchor='center')

random_but = Button(mainscreen, text='Random Game', width=25, height=2, command=lambda: random_game(mainscreen))
random_but.place(relx=0.5, rely=0.5, anchor='center')

quit_but = Button(mainscreen, text='Quit', width=25, height=2, command=mainscreen.quit)
quit_but.place(relx=0.5, rely=0.9, anchor='center')

def exit(event):
    if event.keysym == 'Escape':
        mainscreen.attributes('-fullscreen', False)
        quit()

buttons = [fullscreen, snake_but, black_but, tet_but, quit_but, random_but]
for button in buttons:
    default_color(button)

mainscreen.bind('<KeyPress>', exit)
mainscreen.mainloop()
