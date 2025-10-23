"""A simple blackjack game.

Get as close to 21, but don't go over.
Ace is 1 if there is a risk of going over 21, otherwise 11.
Face cards are 10.
I used X to represent 10.
Player can Hit or Stand.
If player goes over 21, they bust and lose.
If player gets 5 cards without busting, they win automatically.
Dealer must hit until their hand is at least 17.
Good luck.
"""

import random
from turtle import Screen, Turtle
import time


def start_black():
    """Start the blackjack game."""
    delay = 0.1
    maxvalue = 21
    aimax = 17
    values = {'J': 10, 'Q': 10, 'K': 10, 'X': 10}  # Include 'X' for 10 cards
    k = 2  # Counter for number of cards drawn by player
    playing = True
    endfont = ("Arial", 25, "bold")

    def calculate_hand_value(cards, values, maxvalue):
        value = 0
        aces = 0
        for card in cards:
            if card.name == 'A':
                value += 11
                aces += 1
            elif card.name in values:
                value += values[card.name]
            else:
                value += int(card.name)
        while value > maxvalue and aces:
            value -= 10
            aces -= 1
        return value

    # Set up screen
    casino = Screen()
    casino.title("Blackjack")
    casino.bgcolor("#4E6A54")
    casino.setup(width=800, height=600)
    casino.tracer(0)
    casinotk = casino.getcanvas().winfo_toplevel()
    casinotk.attributes("-fullscreen", True)
    casino.onkey(casino.bye, "Escape")

    backcard = Turtle()
    backcard.hideturtle()
    backcard.speed(0)
    backcard.color("white")
    backcard.fillcolor("#A00000")
    backcard.penup()
    backcard.goto(-225, 175)
    backcard.pendown()
    backcard.begin_fill()
    for _ in range(2):
        backcard.forward(100)
        backcard.right(90)
        backcard.forward(150)
        backcard.right(90)
    backcard.end_fill()
    backcard.penup()

    guide = Turtle()
    guide.hideturtle()
    guide.penup()
    guide.speed(0)
    guide.goto(-450, 80)
    guide.color("black")
    guide.write("Dealer Cards:", align="center", font=("Arial", 18, "bold"))
    guide.goto(-450, -100)
    guide.write("Player Cards:", align="center", font=("Arial", 18, "bold"))

    quit = Turtle()  # The quit button
    quit.hideturtle()
    quit.color("#A00000")
    quit.fillcolor("#A00000")
    quit.penup()
    quit.goto(-500, 450)
    quit.write("Press 'Esc' to Quit", align="center",
               font=("Arial", 15, "normal"))
    quit.goto(-500, 430)
    quit.write("(Progress is not saved)", align="center",
               font=("Arial", 10, "normal"))
    quit.goto(-550, 410)
    quit.pendown()
    quit.begin_fill()
    for _ in range(2):
        quit.forward(100)
        quit.right(90)
        quit.forward(40)
        quit.right(90)
    quit.end_fill()
    quit.penup()
    quit.goto(-500, 380)
    quit.color("black")
    quit.write("Quit", align="center", font=("Arial", 12, "bold"))

    def quit_game(x, y):
        if -550 <= x <= -450 and 370 <= y <= 410:
            casino.bye()

    pen = Turtle()
    pen.speed(0)
    pen.color("black")
    pen.penup()
    pen.hideturtle()

    instructions = Turtle()
    instructions.hideturtle()
    instructions.penup()
    instructions.speed(0)
    instructions.goto(0, 260)
    instructions.write("Welcome to Blackjack! Try to get as close to 21 " +
                       "as possible without going over. " +
                       "Press 'HIT' to draw a card or 'STAND' to hold.",
                       align="center", font=("Arial", 18, "bold"))


    class Card():
        # Credit to TokyoEdTech for the Card and Deck classes
        # https://www.youtube.com/watch?v=J8dkgM2g1hY
        def __init__(self, name, suit):
            self.name = name
            self.suit = suit
            self.symbols = {"D": "♦", "C": "♣", "H": "♥", "S": "♠"}

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
                    pen.color("#d00000")
                else:
                    pen.color("black")
                pen.goto(x-18, y-30)
                pen.write(self.symbols[self.suit], False,
                          font=("Consolas", 48, "normal"))
                pen.goto(x-40, y+45)
                pen.write(self.name, False,
                          font=("Consolas", 18, "normal"))
                pen.goto(x-40, y+25)
                pen.write(self.symbols[self.suit], False,
                          font=("Consolas", 18, "normal"))
                pen.goto(x+30, y-60)
                pen.write(self.name, False,
                          font=("Consolas", 18, "normal"))
                pen.goto(x+30, y-80)
                pen.write(self.symbols[self.suit], False,
                          font=("Consolas", 18, "normal"))

    class Deck():
        def __init__(self):
            self.cards = []

            names = ("A", "K", "Q", "J", "X", "9",
                     "8", "7", "6", "5", "4", "3", "2")
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
            names = ("A", "K", "Q", "J", "X", "9",
                     "8", "7", "6", "5", "4", "3", "2")
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

    # Deal initial cards
    start_x = -300
    for i in range(2):
        card = deck.get_card()
        player_cards.append(card)
        card.render(start_x + i * 125, -70, pen)
    card = deck.get_card()
    ai_cards.append(card)
    card.render(-300, 100, pen)
    player_value = calculate_hand_value(player_cards, values, maxvalue)
    ai_value = calculate_hand_value(ai_cards, values, maxvalue)

    # Hit and Stand buttons
    hit = Turtle()
    hit.hideturtle()
    hit.penup()
    hit.speed(0)
    hit.goto(-300, -400)
    hit.fillcolor("lightblue")
    hit.begin_fill()
    for _ in range(2):
        hit.forward(150)
        hit.left(90)
        hit.forward(75)
        hit.left(90)
    hit.end_fill()
    hit.goto(-225, -380)
    hit.color("black")
    hit.write("HIT", align="center", font=("Arial", 25, "bold"))
    hit.color("white")

    stand = Turtle()
    stand.hideturtle()
    stand.penup()
    stand.speed(0)
    stand.goto(150, -400)
    stand.fillcolor("lightblue")
    stand.begin_fill()
    for _ in range(2):
        stand.forward(150)
        stand.left(90)
        stand.forward(75)
        stand.left(90)
    stand.end_fill()
    stand.goto(225, -380)
    stand.color("black")
    stand.write("STAND", align="center", font=("Arial", 25, "bold"))
    stand.color("white")

    # Functions for button clicks
    def hit_click(x, y):
        nonlocal player_value
        nonlocal k
        nonlocal playing
        if playing is False:
            return
        if -300 <= x <= -150 and -400 <= y <= -325:
            card = deck.get_card()
            player_cards.append(card)
            card.render(-300 + k * 125, -70, pen)
            k += 1
            player_value = calculate_hand_value(player_cards, values, maxvalue)
            print(f"Player value: {player_value}")
            pen.goto(0, -300)
            pen.color("black")
            if player_value > maxvalue:
                pen.write("You Bust! Press Space to Play Again",
                          align="center", font=endfont)
                casino.onkey(reset_game, "space")
                playing = False
                casino.listen()
            elif k == 5 and player_value <= maxvalue:
                pen.write("Five Card Charlie! You Win!" +
                          " Press Space to Play Again",
                          align="center", font=endfont)
                casino.onkey(reset_game, "space")
                playing = False
                casino.listen()

    def stand_click(x, y):
        if 150 <= x <= 300 and -400 <= y <= -325:
            pen.color("black")
            nonlocal ai_value, playing, player_value
            pen.goto(0, -300)
            if not playing:
                return
            if player_value == maxvalue and k == 2:
                pen.write("Blackjack! You Win! Press Space to Play Again",
                          align="center", font=endfont)
            else:
                while ai_value < aimax and ai_value < player_value:
                    card = deck.get_card()
                    ai_cards.append(card)
                    card.render(-425 + len(ai_cards) * 125, 100, pen)
                    ai_value = calculate_hand_value(ai_cards, values, maxvalue)
                    print(f"AI value: {ai_value}")
                    pen.goto(0, -300)
                    pen.color("black")
                if ai_value > maxvalue:
                    pen.write("Dealer Busts! You Win!" +
                              " Press Space to Play Again",
                              align="center", font=endfont)
                elif ai_value == player_value:
                    pen.write("It's a Tie! Press Space to Play Again",
                              align="center", font=endfont)
                elif ai_value > player_value:
                    pen.write("Dealer Wins! Press Space to Play Again",
                              align="center", font=endfont)
                else:
                    pen.write("You Win! Press Space to Play Again",
                              align="center", font=endfont)
            playing = False
            casino.onkey(reset_game, "space")
            casino.listen()

    # Reset the game.
    def reset_game():
        casino.clearscreen()
        start_black()

    def button_click(x, y):
        hit_click(x, y)
        stand_click(x, y)
        quit_game(x, y)

    casino.onclick(button_click)
    casino.listen()
    casinotk.protocol("WM_DELETE_WINDOW", casino.bye)
    casino.mainloop()
    time.sleep(delay)

# Start the game if this file is run directly
if __name__ == "__main__":
    start_black()
