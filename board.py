import random
from helpers import Deck
from helpers import Player

TILES_NAMES = ["Stone", "Stone", "Stone", "Sheep", \
"Sheep", "Sheep", "Sheep", "Wheat", "Wheat", "Wheat", \
"Wheat", "Brick", "Brick", "Brick", "Desert"]

TILES_NUMS = [2, 3, 3, 4, 4, 5, 5, 6, 6, \
8, 8, 9, 9, 10, 10, 11, 11, 12]

##################
#     ROAD IDS   #
#       /\       #
#      /  \      #
#     0    1     #
#    /      \    #
#   |        |   #
#   5        2   #
#   |        |   #
#   |        |   #
#    \      /    #
#     4    3     #
#      \  /      #
#       \/       #
##################

TILES_ROADS_UPPER_LEFT = 0
TILES_ROADS_UPPER_RIGHT = 1
TILES_ROADS_RIGHT = 2
TILES_ROADS_LOWER_RIGHT = 3
TILES_ROADS_LOWER_LEFT = 4
TILES_ROADS_LEFT = 5


##################
#     SPOT IDS   #
#       /0       #
#      /  \      #
#     /    \     #
#    /      \    #
#   5        1   #
#   |        |   #
#   |        |   #
#   |        |   #
#    4      2    #
#     \    /     #
#      \  /      #
#       \3       #
##################

TILES_SPOTS_UPPER = 0
TILES_SPOTS_UPPER_RIGHT = 1
TILES_SPOTS_LOWER_RIGHT = 2
TILES_SPOTS_LOWER = 3
TILES_SPOTS_LOWER_LEFT = 4
TILES_SPOTS_UPPER_LEFT = 5

class Tile:
    dice_num = 0
    resource_name = ""


    def __init__(self, resource_name, dice_num):
        self.resource_name = resource_name
        self.dice_num = dice_num

    def __str__(self):
        return self.resource_name + " " + str(self.dice_num)


class Board:
    players = []
    tiles = []
    deck = Deck()

    def __init__(self, players):
        for x in players:
            self.players.append(Player(x))
            print x
        
        random.shuffle(TILES_NUMS)
        random.shuffle(TILES_NAMES)

        i = 0
        
        for x in range(len(TILES_NAMES)):
            tile_name = TILES_NAMES[x]
            if (tile_name != "Desert"):
                self.tiles.append(Tile(tile_name, TILES_NUMS[i]))
                i = i + 1
            else:
                self.tiles.append(Tile("Desert", 0))

        deck.deckShuffle()
        


Board(["megan", "julia", "mom"])
