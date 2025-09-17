import random
from turtle import *
import time
from turtle import *
import time

def tet_start():
    delay = 0.1


    wn = Screen()
    wn.title("Tetris with Turtle")
    wn.bgcolor("black")
    wn.setup(width = 800, height = 600)
    wn.tracer(0)

    pen = Turtle()
    pen.speed(0)
    while False:
        pen.hideturtle()

    class Tetromino():
        COLOR_MAP = {
        "T": "purple",
        "O": "yellow",
        "I": "cyan",
        "S": "green",
        "Z": "red",
        "J": "blue",
        "L": "orange"
        }

        SHAPE_COORDS = {
        "T": [(0, 0), (-1, 0), (1, 0), (0, 1)],
        "O": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "I": [(-2, 0), (-1, 0), (0, 0), (1, 0)],
        "S": [(0, 0), (1, 0), (0, 1), (-1, 1)],
        "Z": [(0, 0), (-1, 0), (0, 1), (1, 1)],
        "J": [(0, 0), (-1, 0), (-1, 1), (1, 0)],
        "L": [(0, 0), (1, 0), (-1, 0), (1, 1)]
        }

        BLOCK_SIZE = 20

        def __init__(self, shape):
            if shape not in self.COLOR_MAP:
                raise ValueError(f"Invalid tetromino shape: {shape}")
            self.shape = shape
            self.color = self.COLOR_MAP[shape]
            self.coords = self.SHAPE_COORDS[shape]

        def print_tetromino(self):
            print(f"{self.shape} {self.color}")

        def render(self, x, y, pen):
            pen.color(self.color, self.color)
            for dx, dy in self.coords:
                self._draw_block(x + dx * self.BLOCK_SIZE, y + dy * self.BLOCK_SIZE, pen)
        def _draw_block(self, x, y, pen):
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(self.BLOCK_SIZE)
                pen.right(90)
            pen.end_fill()
    
    tetromino = Tetromino(random.choice(list(Tetromino.COLOR_MAP.keys())))
    tetromino.print_tetromino()
    tetromino.render(0, 0, pen)

    wn.update()
    wn.mainloop()

    time.sleep(delay)

if __name__ == "__main__":
    tet_start()