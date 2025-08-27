import tkinter as tk
import random

def toggle_fullscreen(window):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)


mainscreen = tk.Tk()
mainscreen.title('Just another game compendium')
mainscreen.geometry("800x600")

fullscreen = tk.Button(mainscreen, text='Fullscreen', width = 10, command = lambda: toggle_fullscreen(mainscreen))
fullscreen.pack()

def key_press(event):
    if event.keysym == 'Escape':
        mainscreen.attributes('-fullscreen', False)
        quit()

mainscreen.bind('<KeyPress>', key_press)
mainscreen.mainloop()
