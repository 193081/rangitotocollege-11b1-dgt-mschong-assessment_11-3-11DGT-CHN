from tkinter import *
import black
import snake
import tet
from random import randint

def toggle_fullscreen(window):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def default_color(item):
    item.configure(bg='black', fg='white', font=('Arial', 10) )

def random_game(window):
    i = randint(0,3)
    if i == 0:
        snake.start_snek()
    elif i == 1:
        black.start_black()
    elif i == 2:
        tet.tet_start()
    elif i == 3:
        window.quit()

mainscreen = Tk()
mainscreen.title('Just another game compendium')
mainscreen.configure(bg='black')
mainscreen.geometry("800x600")

title_label = Label(mainscreen, text='Game Compendium', bg='black', fg='white', font=('Arial', 24, 'bold'))
title_label.pack(pady=20)

fullscreen = Button(mainscreen, text ='Fullscreen', width = 25, height = 10, command = lambda: toggle_fullscreen(mainscreen, fullscreen))
fullscreen.place(relx=0.75, rely=0.66, anchor='center')

snake_but = Button(mainscreen, text ='Snake', width = 25, height = 10, command = lambda: snake.start_snek())
snake_but.place(relx=0.25, rely=0.33, anchor='center')

black_but = Button(mainscreen, text ='Blackjack', width = 25, height = 10, command = lambda: black.start_black())
black_but.place(relx=0.25, rely=0.66, anchor='center')

tet_but = Button(mainscreen, text = 'Tetris', width = 25, height = 10, command = lambda: tet.tet_start())
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
