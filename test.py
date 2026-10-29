from main import *

def test_should_return_card_value():
    card = Card(2, "Pique")
    assert card.return_value() == 2

def test_should_return_card_suit():
    card = Card(2, "Pique")
    assert card.return_suit() == "Pique"

def test_should_return_brelan_points():
    card1 = Card(2, "Pique")
    card2 = Card(2, "Coeur")
    card3 = Card(2, "Carreau")
    card4 = Card(3, "Trèfle")
    card5 = Card(4, "Trèfle")
    main = [card1, card2, card3, card4, card5]
    assert combinaison(main) == 30

def test_should_return_brelan_points_with_3_first_cards():
    card1 = Card(2, "Pique")
    card2 = Card(4, "Coeur")
    card3 = Card(2, "Carreau")
    card4 = Card(3, "Trèfle")
    card5 = Card(2, "Trèfle")
    main = [card1, card2, card3, card4, card5]
    assert combinaison(main) == 30