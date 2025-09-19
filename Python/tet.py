import random
from turtle import *
import time

def tet_start():
    DELAY = 0.1


    wn = Screen()
    wn.title("Tetris with Turtle")
    wn.bgcolor("black")
    wn.setup(width = 0.9, height = 1.0)
    wn.tracer(0)

    pen = Turtle()
    pen.speed(0)
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

    pos_x = 0
    pos_y = 200

    BOARD_COLS = 10
    BOARD_ROWS = 20

    def draw_grid(pen):
        pen.color("gray")
        # vertical lines
        for x in range(BOARD_COLS + 1):
            pen.penup()
            pen.goto(-BOARD_COLS * Tetromino.BLOCK_SIZE // 2 + x * Tetromino.BLOCK_SIZE,
                    -BOARD_ROWS * Tetromino.BLOCK_SIZE // 2)
            pen.pendown()
            pen.goto(-BOARD_COLS * Tetromino.BLOCK_SIZE // 2 + x * Tetromino.BLOCK_SIZE,
                    BOARD_ROWS * Tetromino.BLOCK_SIZE // 2)

        # horizontal lines
        for y in range(BOARD_ROWS + 1):
            pen.penup()
            pen.goto(-BOARD_COLS * Tetromino.BLOCK_SIZE // 2,
                    -BOARD_ROWS * Tetromino.BLOCK_SIZE // 2 + y * Tetromino.BLOCK_SIZE)
            pen.pendown()
            pen.goto(BOARD_COLS * Tetromino.BLOCK_SIZE // 2,
                    -BOARD_ROWS * Tetromino.BLOCK_SIZE // 2 + y * Tetromino.BLOCK_SIZE)

    def game_loop():
        nonlocal pos_y, tetromino

        pen.clear()
        draw_grid(pen)
        tetromino.render(pos_x, pos_y, pen)

        # drop piece
        pos_y -= Tetromino.BLOCK_SIZE

        # bottom of the board
        if pos_y < -(BOARD_ROWS // 2) * Tetromino.BLOCK_SIZE + 20:
            tetromino = Tetromino(random.choice(list(Tetromino.COLOR_MAP.keys())))
            pos_y = (BOARD_ROWS // 2) * Tetromino.BLOCK_SIZE

        wn.update()
        wn.ontimer(game_loop, 500)

    game_loop()
    wn.mainloop()

    time.sleep(DELAY)

if __name__ == "__main__":
    tet_start()