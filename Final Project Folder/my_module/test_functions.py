from module import *

def test_validate_card():
    valid_suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    card_a = Card(3,'Clubs')
    card_a.validate_card(3, 'Clubs')

    assert display_card(card_a) == ('3', 'Clubs')
    assert card_a.value == 3 or '3'
    assert card_a.suit == 'Clubs'
    assert card_a.value in valid_values
    assert card_a.suit in valid_suits
        


def test_build_deck():
       
    test_deck = Deck()
    test_deck.build_deck([])

    valid_suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    assert len(test_deck.full_deck) == 52
    assert len(test_deck.remaining_cards) == 52
    assert len(test_deck.drawn) == 0
    for cards in test_deck.full_deck:
        assert cards.suit in valid_suits
        assert cards.value in valid_values
            

def test_draw():
 
    valid_suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
    valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    test_deck = Deck()


    assert len(test_deck.draw(2)) == 2
    assert len(test_deck.remaining_cards) == 50
    for cards in test_deck.remaining_cards:
        assert cards.suit in valid_suits
        assert cards.value in valid_values
