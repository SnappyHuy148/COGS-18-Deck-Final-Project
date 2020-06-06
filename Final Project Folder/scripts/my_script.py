"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.module import *

# Here we create an instance of our Deck
Deck = Deck()

print("Let's say we would like to draw some cards from the deck say to play Blackjack so let's draw 2 cards")
input('Press Enter to Draw 2 cards\n')
Deck.draw(2)
Deck.show_drawn()

print("Now we could draw an additional card if we wanted to. This would mean we have drawn a total of 3 cards from our Deck")
input('Press Enter to draw another card \n')
Deck.draw()
Deck.show_drawn()

print('\n')

print("Did we win or lose? Either way we should just restack the deck for the next person to use. They wouldn't be able to play without a full deck")
input('Press enter to refill the deck with cards')
Deck.stack_deck()

print('Now the deck is full of all of its cards again ready for someone else to draw from it')

print('\n')

print("Let's play a simple game then. You are going to draw a card and guess the suit of the card drawn")

guess_suit()

print('\n')

print('Did you guess it right? Well it was a 1 in 4 chance so maybe you were lucky. Now we are done playing with our cards')
