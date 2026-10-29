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
    if estCarre(cards):
        return 60
    if estFull(cards):
        return 50
    if estBrelan(cards):
        return 30
    if estSuite(cards):
        return 40
    if estCouleur(cards):
        return 45
    tri = sorted(card.value for card in cards)
    return tri[4]


def estBrelan(cards):
    occurrences_value = Counter([card.value for card in cards])
    if occurrences_value.most_common(1)[0][1] == 3:
        return True
    return False

def estCarre(cards):
    occurrences_value = Counter([card.value for card in cards])
    if occurrences_value.most_common(1)[0][1] == 4:
        return True
    return False

def estFull(cards):
    occurrences = Counter([card.value for card in cards])
    return sorted(occurrences.values()) == [2, 3]

def estCouleur(cards):
    occurrences_color = Counter([card.suit for card in cards])
    return occurrences_color.most_common(1)[0][1] == 4

def estSuite(cards):
    tri = sorted(card.value for card in cards)
    return tri[0] == tri[1]-1 == tri[2]-2 == tri[3]-3 == tri[4]-4