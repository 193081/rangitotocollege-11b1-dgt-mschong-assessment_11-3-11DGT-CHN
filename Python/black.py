import random
from turtle import *
import time


def start_black():

    delay = 0.1
    score = 100
    high_score = 100
    maxvalue = 21
    aimax = 17
    values = {'J': 10, 'Q': 10, 'K': 10}

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

    #Credit to TokyoEdTech for the card rendering code
    class Card():
        def __init__(self, name, suit):
            self.name = name
            self.suit = suit
            self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
            
        def print_card(self):
            print(f"{self.name}{self.symbols[self.suit]}")
            
        def render(self, x, y, pen):
            # Draw border
            pen.penup()
            pen.goto(x, y)
            pen.color("white")
            pen.goto(x-50, y+75)
            pen.begin_fill()
            pen.pendown()
            pen.goto(x+50, y+75)
            pen.goto(x+50, y-75)
            pen.goto(x-50, y-75)
            pen.goto(x-50, y+75)
            pen.end_fill()
            pen.penup()
            
            if self.name != "":
                # Draw suit in the middle
                if self.suit in ("H", "D"):
                    pen.color("red")
                else:    
                    pen.color("black")
                pen.goto(x-18, y-30)
                pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
                
                # Draw top left 
                pen.goto(x-40, y+45)
                pen.write(self.name, False, font=("Courier New", 18, "normal"))
                pen.goto(x-40, y+25)
                pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
                
                # Draw bottom right
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
            card = self.cards.pop()
            return card
            
        def reset(self):
            self.cards = []
            
            names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
            suits = ("D", "C", "H", "S")
            
            for name in names:
                for suit in suits:
                    card = Card(name, suit)
                    self.cards.append(card)
            
            self.shuffle()
            
    # Create deck                
    deck = Deck()

    # Shuffle deck
    deck.reset()

    time.sleep(delay)

    player_cards = []
    ai_cards = []
    player_value = 0
    ai_value = 0
    
    start_x = -250
    for x in range(2):
        card = deck.get_card()
        card.render(start_x + x * 125, 0, pen)


    wn.mainloop()

