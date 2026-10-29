from collections import Counter


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def return_value(self):
        return self.value

    def return_suit(self):
        return self.suit

def combinaison(cards):
    occurrences = Counter([card.value for card in cards])
    if occurrences.most_common(1)[0][1] == 4:
        return 60
    if occurrences.most_common(1)[0][1] == 3:
        return 30
    for _ in cards:
        if cards[0].value == cards[1].value-1 == cards[2].value-2 == cards[3].value-3 == cards[4].value-4:
            return 40

    return None
