import time

from game.player import Player
from game.world.world import World

from custom.game import CustomGame

class Game ():

    def __init__(self):
        # Init Model Time  
        self.gameTimeStart = time.time()      
        
        self.cg = CustomGame()
        
        
        
    def update(self):
        self.cg.updateGame()

    def handlePlayerInput(self, input):
        self.cg.handlePlayerInput(input)

    def get_gameTimeStamp(self):
        return time.time() - self.gameTimeStart


    def __getstate__(self):
        state = self.__dict__.copy()
        # Don't pickle vlm
        # del state["vlm"]
        return state
    

    def __setstate__(self, state):
        self.__dict__.update(state)

    