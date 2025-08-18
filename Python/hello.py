import tkinter as tk
import random

screen = tk.Tk()
screen.attributes('-fullscreen', True)

block
def key_press(event):
    if event.keysym == 'Escape':
        screen.attributes('-fullscreen', False)
        quit()

screen.bind('<KeyPress>', key_press)
screen.mainloop()
