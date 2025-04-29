from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self): # checks if all cards have the same suit
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit: # checks the suit and compares it
                return False # if one card is different it's false
        return True # if its a flush

    @property
    def is_full_house(self):
        return self.number_matches == 8 # it checks if the number of matching ranks is exactly 8

    @property
    def number_matches(self): # counts how many matches exist between card ranks in the hand
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.number_matches == 2: # one pair found
            return True
        return False

    @property
    def is_two_pair(self):
        return self.number_matches == 4 # two pairs (more advanced)

    @property
    def is_trips(self):
        if self.number_matches == 6: # three cards of the same rank
            return True
        return False

    @property
    def is_quads(self):
        if self.number_matches == 12: # four cards share the same rank
            return True
        return False

    @property
    def is_straight(self): # calculates the distance between the highest and lowest card ranks
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

count = 0 # tracks the total number of hands generated
matches = 0 # tracks the number of hands that are straights
while matches < 10: # loop keeps running until it finds 10 straights
    deck = Deck() # new deck
    deck.shuffle() # shuffles the deck
    hand = PokerHand(deck) # deals a poker hand
    if hand.is_straight:
        matches += 1 # increase matches by one
        print(hand)
    count += 1 # after every hand (straight ot noy) increase count by one

print(f"probability of a full straight is {100*matches/count}%") # how often a straight occurred during the simulation