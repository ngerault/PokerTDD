class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_value(self):
        return self.value

    def return_suit(self):
        return self.suit

def combinaison(cards):
    for _ in cards:
        if cards[0].value == cards[1].value == cards[2].value:
            return 30
    return None
