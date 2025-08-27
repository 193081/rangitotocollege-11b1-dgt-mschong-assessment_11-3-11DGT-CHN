import tkinter as tk
import random

menu = tk.Tk()
menu.attributes('-fullscreen', True)

def key_press(event):
    if event.keysym == 'Escape':
        menu.attributes('-fullscreen', False)
        quit()

menu.bind('<KeyPress>', key_press)
menu.mainloop()
