from tkinter import *
import black
import snake
import tet

button = []

def toggle_fullscreen(window):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def hide_all():
    for b in button:
        b.place_forget()

mainscreen = Tk()
mainscreen.title('Just another game compendium')
mainscreen.geometry("800x600")

fullscreen = Button(mainscreen, text ='Fullscreen', width = 25, height = 10, command = lambda: toggle_fullscreen(mainscreen))
fullscreen.place(x=400, y=400)

snake_but = Button(mainscreen, text ='Snake', width = 25, height = 10, command = lambda: [snake.start_snek, hide_all()])
snake_but.place(x=200, y=200)

black_but = Button(mainscreen, text ='Blackjack', width = 25, height = 10, command = lambda: [black.start_black, hide_all()])
black_but.place(x=200, y=400)

tet_but = Button(mainscreen, text = 'Tetris', width = 25, height = 10, command = lambda: [tet.tet_start, hide_all()])
tet_but.place(x=400, y=200)

button.extend([snake_but, fullscreen, black_but, tet_but])

def exit(event):
    if event.keysym == 'Escape':
        mainscreen.attributes('-fullscreen', False)
        quit()

mainscreen.bind('<KeyPress>', exit)
mainscreen.mainloop()
