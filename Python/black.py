import random
from turtle import *
import time


def start_black():
    delay = 0.1
    score = 100
    high_score = 100
    maxvalue = 21
    aimax = 17
    values = {'J': 10, 'Q': 10, 'K': 10, 'T': 10}  # Include 'T' for 10 cards
    player_value = 0  # Initialize player's hand value
    k = 0

    wn = Screen()
    wn.title("Blackjack with Turtle")
    wn.bgcolor("green")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    frame = Turtle()
    frame.hideturtle()
    frame.color("white")   
    frame.penup()
    frame.goto(-410, -410)
    frame.pendown()
    for i in range(4):
        frame.forward(820)
        frame.left(90)

    pen = Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 300)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

#Credit to TokyoEdTech for the Card and Deck classes
#https://www.youtube.com/watch?v=J8dkgM2g1hY
    class Card():
        def __init__(self, name, suit):
            self.name = name
            self.suit = suit
            self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}

        def print_card(self):
            print(f"{self.name}{self.symbols[self.suit]}")

        def render(self, x, y, pen):
            pen.penup()
            pen.goto(x-50, y+75)
            pen.color("white")
            pen.begin_fill()
            pen.pendown()
            pen.goto(x+50, y+75)
            pen.goto(x+50, y-75)
            pen.goto(x-50, y-75)
            pen.goto(x-50, y+75)
            pen.end_fill()
            pen.penup()

            if self.name != "":
                if self.suit in ("H", "D"):
                    pen.color("red")
                else:    
                    pen.color("black")
                pen.goto(x-18, y-30)
                pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
                pen.goto(x-40, y+45)
                pen.write(self.name, False, font=("Courier New", 18, "normal"))
                pen.goto(x-40, y+25)
                pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
                pen.goto(x+30, y-60)
                pen.write(self.name, False, font=("Courier New", 18, "normal"))
                pen.goto(x+30, y-80)
                pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))

    class Deck():
        def __init__(self):
            self.cards = []

            names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
            suits = ("D", "C", "H", "S")

            for name in names:
                for suit in suits:
                    card = Card(name, suit)
                    self.cards.append(card)

        def shuffle(self):
            random.shuffle(self.cards)

        def get_card(self):
            return self.cards.pop()

        def reset(self):
            self.cards = []
            names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
            suits = ("D", "C", "H", "S")
            for name in names:
                for suit in suits:
                    card = Card(name, suit)
                    self.cards.append(card)
            self.shuffle()

    deck = Deck()
    deck.reset()

    player_cards = []
    ai_cards = []

    # Deal 2 initial cards
    start_x = -250
    for i in range(2):
        card = deck.get_card()
        player_cards.append(card)
        card.render(start_x + i * 125, 0, pen)
        # Calculate player value
        if card.name in values:
            player_value += values[card.name]
        elif card.name == 'A':
            if player_value + 11 > maxvalue:
                player_value += 1
            else:
                player_value += 11
        else:
            player_value += int(card.name)

    hit = Turtle()
    hit.hideturtle()
    hit.penup()
    hit.speed(0)
    hit.goto(-100, -150)
    hit.fillcolor("lightblue")
    hit.begin_fill()
    for _ in range(2):
        hit.forward(100)
        hit.left(90)
        hit.forward(40)
        hit.left(90)
    hit.end_fill()
    hit.goto(-50, -140)
    hit.color("black")
    hit.write("HIT", align="center", font=("Courier", 20, "bold"))
    hit.color("white")

    stand = Turtle()
    stand.hideturtle()
    stand.penup()
    stand.speed(0)
    stand.goto(100, -100)
    stand.fillcolor("lightblue")
    stand.begin_fill()
    for _ in range(2):
        stand.forward(100)
        stand.left(90)
        stand.forward(40)
        stand.left(90)
    stand.end_fill()
    stand.goto(150, -90)
    stand.color("black")
    stand.write("STAND", align="center", font=("Courier", 20, "bold"))
    stand.color("white")

    def hit_click(x, y):
        nonlocal player_value
        if -100 <= x <= 0 and -150 <= y <= -110:
            card = deck.get_card()
            player_cards.append(card)
            card.render(-250 + len(player_cards) * 125, 0, pen)
            if card.name in values:
                player_value += values[card.name]
            elif card.name == 'A':
                if player_value + 11 > maxvalue:
                    player_value += 1
                else:
                    player_value += 11
            else:
                player_value += int(card.name)
            print(f"Player value: {player_value}")

            if player_value > maxvalue:
                pen.color("black")
                pen.goto(0, -250)
                pen.write("You Bust! Press Space to Play Again", align="center", font=("Courier", 18, "normal"))
                wn.onkey(reset_game, "space")
                wn.listen()

    def stand_click(x, y):
        if 100 <= x <= 200 and -100 <= y <= -60:
            pen.color("black")
            pen.goto(0, -250)
            if player_value == maxvalue:
                pen.write("Blackjack! You Win! Press Space to Play Again", align="center", font=("Courier", 18, "normal"))
            else:
                pen.write(f"You Stand at {player_value}. Press Space to Play Again", align="center", font=("Courier", 18, "normal"))
            wn.onkey(reset_game, "space")
            wn.listen()

    def reset_game():
        wn.clearscreen()
        start_black()

    def button_click(x, y):
        hit_click(x, y)
        stand_click(x, y)

    wn.onclick(button_click)
    wn.listen()
    wn.mainloop()

if __name__ == "__main__":
    start_black()