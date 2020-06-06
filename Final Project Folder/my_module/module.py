"""A collection of classes and functions for doing my project."""
from random import choice
from copy import deepcopy

class Card():
    
    def __init__(self, value, suit):
        """ 
        Creates an instance of our Card class 
    
        Parameters
        ----------
        value: string
            The value of the card ranging from 1-10 and Jack/Queen/King
        
        suit : string
            The suit of the Card which ranges from Clubs/Spades/Hearts/Diamonds
    
        """
        self.validate_card(value, suit)
        self.value = value
        self.suit = suit
        
    #Checks if the card has a valid suit and value    
    def validate_card(self, value, suit):
        
        valid_suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        valid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        if suit not in valid_suits:
            raise TypeError('Card must have a valid Suit ranging from Clubs/Spades/Hearts/Diamonds')
            
        if value not in valid_values:
            raise ValueError('Card must have a valid Value ranging from 1 - 10 or Jack/Queen/King')

def display_card(card):
    return str(card.value), card.suit 


class Deck():
   
    def __init__(self):
        """ 
        Creates an instance of our Deck Class
        
        """
        self.full_deck = self.build_deck([])
        self.drawn = []
        self.remaining_cards = self.build_deck([])
        self.stack_deck()
    
    #Fills the deck with the 52 cards of each suit and value. 
    def build_deck(self, deck):
        for value in range(1,11):
            for suit in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
                deck.append(Card(value,suit))
        
        for value in ['Jack', 'Queen', 'King']:
            for suit in ['Clubs', 'Spades', 'Hearts', 'Diamonds']:
                deck.append(Card(value,suit))
        return deck
    
    #Show what cards are remaining in the Deck
    def show_deck(self):
        for cards in self.remaining_cards:
            print(display_card(cards))
    
    #Stacks the deck with all of its cards and empties the drawn cards pile
    def stack_deck(self):
        self.remaining_cards = deepcopy(self.full_deck)
        self.drawn = []
        
            
    #Draw a random card from the deck a number of times without drawing any duplicates and remove it from the deck      
    def draw(self, number = 1):
        if isinstance(number, int):
            counter = 0
            if number <0 or number > 52:
                raise IndexError('Can only draw a whole number 1 through 52 cards from the deck')
            while counter < number and len(self.drawn) < 52:
                random_choice = choice(range(len(self.remaining_cards)))
                random_card = self.remaining_cards[random_choice]
                self.drawn.append(random_card)
                self.remaining_cards.remove(random_card)
                counter += 1
        else:
            raise TypeError('Parameter must be an integer between 1 and 52')
       
        if len(self.drawn) >= 52:
            print('You have drawn all of the cards')
        
        return self.drawn
            
    #Show what cards have been drawn from the deck
    def show_drawn(self):
        for cards in self.drawn:
            print(display_card(cards))
        if len(self.drawn) >= 52:
            print('You have drawn all of the cards')


def guess_suit():
    
    deck = Deck()
    deck.draw()
    card_suit = deck.drawn[0]
    guess = input('Guess the Suit: ')
    
    deck.show_drawn()
    if str(guess) == card_suit.suit:
        print('You guessed the right value!')
    else:
        print('Looks like you guessed the wrong value')