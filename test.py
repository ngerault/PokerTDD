from main import Card

def test_should_return_card_value():
    card = Card(2, "Pique")
    assert card.return_value() == 2

def test_should_return_card_suit():
    card = Card(2, "Pique")
    assert card.return_suit() == "Pique"