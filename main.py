import random, time

money = 100
placed = 50
dealer_hand = []
player_hand = []

# valid cards
cards = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
    "Ace"
]

def get_card():
    return random.choice(cards)

def get_bet(): # Get user input, if not valid (e.g. too high/NaN) then retry
    return 50

def game():
    card = get_card()
    print(cards.index(card), card)


while True:
    game()
    time.sleep(1)
