import random


class Deck:             
    
    def __init__(self):
        self.deck = []

    # Initialize the deck 
    def deckShuffle(self):
        self.deck = 14 * ['knight'] + 5 * ['vp'] + 2 * ['rb'] + \
            2 * ['mono'] + 2 * ['yp']
        random.shuffle(self.deck)
        
        
    # Remove a card from the front of the array     
    def drawCard(self):
        if len(self.deck) == 0:
            return 0
        else:
            temp = self.deck[0]
            self.deck = self.deck[1:]
            return temp
        
        
        
# Player class to keep track of how many points, which dev cards, player name,
# where roads and cities are 
class Player: 
    
    def __init__(self, n):
        self.name = n
        self.cities = []
        self.roads = []
        self.settle = []
        self.devs = {'knight': 0, 'vp': 0, 'rb': 0, 'mono': 0, 'yp': 0}
        
        # 2 if player has longest road or largest army. 0 otherwise
        self.lr = 0
        self.la = 0
        
        self.points = 2 * len(self.cities) + len(self.settle) + self.lr + \
            self.la + self.hand['vp']
        
    
    # d is the deck of dev cards
    def drawDev(self, d):
        card = d.drawCard()
        if card == 0:
            return card
        else:
            self.hand[card] += 1
            return card
        
        
    
    
    