import random

class Card: # template to create objects
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, suit, rank): #the constructor, automatically called when you create a new card
        if rank not in self.RANKS:
            raise ValueError("Invalid rank") #validation
        if suit not in self.SUITS:
            raise ValueError("Invalid suit") #validation
        self._suit = suit # internal use
        self._rank = rank # internal use

    def __eq__(self, other):
        return self.rank == other.rank # two cards are equal if they have the same rank

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank) # checks the ranks and compares the indexes


    def __str__(self):
        return f"{self._rank}{self._suit}" # combines rank and suit into the same string (Qhearts)

    def __repr__(self):
        return self.__str__() # reuses the __str__ method to keep it simple

    @property # hides internal variables and keeps the possibility open for future validation
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

class Deck:
    def __init__(self):
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        return str(self._deck) # defines how the deck will be printed

    def shuffle(self):
        random.shuffle(self._deck) # randomizes order of cards

    def deal(self):
        return self._deck.pop(0) # removes and returns the top cards

if __name__ == "__main__":
    deck = Deck() # creates a new deck
    print(deck) # prints ordered deck
    deck.shuffle() # shuffles the deck
    print(deck) # prints the deck again (now shuffled)
    print(deck.deal()) # deal removes first card and prints it