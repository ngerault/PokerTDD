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
    occurrences_value = Counter([card.value for card in cards])
    if occurrences_value.most_common(1)[0][1] == 4:
        return 60
    if occurrences_value.most_common(1)[0][1] == 3:
        return 30
    tri = sorted(card.value for card in cards)
    if tri[0] == tri[1]-1 == tri[2]-2 == tri[3]-3 == tri[4]-4:
        return 40
    occurrences_color = Counter([card.suit for card in cards])
    if occurrences_color.most_common(1)[0][1] == 4:
        return 45
    return tri[4]
