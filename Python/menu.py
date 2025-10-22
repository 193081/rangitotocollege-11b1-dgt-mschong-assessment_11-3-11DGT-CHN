"""This is the main menu for the game compendium.

I wish I could have used pygame to be honest.
"""

from tkinter import Tk, Label, Button
import subprocess
import sys
from random import randint


def toggle_fullscreen(window):
    """Toggle Fullscreen when clicked."""
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)


def run_game(script_name):
    """Run the game."""
    subprocess.Popen([sys.executable, script_name])


def random_game(window):
    """Random game selection."""
    i = randint(0, 3)
    if i == 0:
        run_game("Python/snake.py")
    elif i == 1:
        run_game("Python/black.py")
    elif i == 2:
        run_game("Python/click.py")
    elif i == 3:
        window.quit()


mainscreen = Tk()


mainscreen.title('Just another game compendium')
mainscreen.configure(bg='black')
mainscreen.geometry("800x600")

title_label = Label(mainscreen, text='Game Compendium', bg='black',
                    fg='white', font=('Arial', 24, 'bold'))
title_label.pack(pady=20)

fullscreen = Button(mainscreen, text='Fullscreen', width=15, height=5,
                    command=lambda: toggle_fullscreen(mainscreen),
                    bg='gray', fg='black', font=('Arial', 15))
fullscreen.place(relx=0.75, rely=0.66, anchor='center')

snake_but = Button(mainscreen, text='Snake', width=15, height=5,
                   command=lambda: run_game("Python/snake.py"), bg='green',
                   fg='black', font=('Arial', 15))
snake_but.place(relx=0.25, rely=0.33, anchor='center')

black_but = Button(mainscreen, text='Blackjack', width=15, height=5,
                   command=lambda: run_game("Python/black.py"), bg='red',
                   fg='black', font=('Arial', 15))
black_but.place(relx=0.25, rely=0.66, anchor='center')

click_but = Button(mainscreen, text='Button clicker', width=15, height=5,
                   command=lambda: run_game("Python/click.py"), bg='blue',
                   fg='white', font=('Arial', 15))
click_but.place(relx=0.75, rely=0.33, anchor='center')

random_but = Button(mainscreen, text='Random Game', width=25, height=2,
                    command=lambda: random_game(mainscreen), bg='yellow',
                    fg='black', font=('Arial', 15))
random_but.place(relx=0.5, rely=0.5, anchor='center')

quit_but = Button(mainscreen, text='Quit', width=10, height=2,
                  command=mainscreen.quit, bg='red', fg='black',
                  font=('Arial', 15))
quit_but.place(relx=0.5, rely=0.9, anchor='center')

text_list = [
    title_label, fullscreen, snake_but, black_but,
    click_but, random_but, quit_but
    ]


def trip(listtext):
    """Make a Suprise."""
    for item in listtext:
        item.configure(font=('Comic Sans MS', 15))


suprise_but = Button(mainscreen, text='Suprise', width=10, height=2,
                     command=lambda: trip(text_list), bg='orange', fg='black',
                     font=('Comic Sans MS', 15))
suprise_but.place(relx=0.5, rely=0.7, anchor='center')


def exit(event):
    """GO AWAY."""
    if event.keysym == 'Escape':
        mainscreen.attributes('-fullscreen', False)
        quit()


mainscreen.bind('<KeyPress>', exit)

mainscreen.mainloop()
