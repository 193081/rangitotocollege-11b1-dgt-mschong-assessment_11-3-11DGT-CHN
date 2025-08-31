from tkinter import *
import black
import snake
import tet

def toggle_fullscreen(window):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)


mainscreen = Tk()
mainscreen.title('Just another game compendium')
mainscreen.geometry("800x600")

fullscreen = Button(mainscreen, text='Fullscreen', width = 10, command = lambda: toggle_fullscreen(mainscreen))
fullscreen.pack()

snake_but = Button(mainscreen, text='Snake', width=10, command=snake.start_snek())
snake_but.pack


def key_press(event):
    if event.keysym == 'Escape':
        mainscreen.attributes('-fullscreen', False)
        quit()

mainscreen.bind('<KeyPress>', key_press)
mainscreen.mainloop()
