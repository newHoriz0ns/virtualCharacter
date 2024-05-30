import time

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QGraphicsItem

from game.player import Player
from game.world.world import World

from custom.game import CustomGame


class Game (QObject):

    sig_gameUpdate = pyqtSignal(int)

    sig_addItem = pyqtSignal(QGraphicsItem)
    sig_removeItem = pyqtSignal(QGraphicsItem)

    def __init__(self):
        super().__init__()
        
        # Init Model Time  
        self.gameTimeStart = time.time()      
        
        self.cg = CustomGame()
        
        # Connects for adding and removing items in View
        self.cg.sig_addItem.connect(self.sig_addItem.emit)
        self.cg.sig_removeItem.connect(self.sig_removeItem.emit)
        
        
    def update(self):
        self.cg.updateGame()
        self.sig_gameUpdate.emit(0)


    def getQuickStats(self):
        return self.cg.getQuickStats()


    def handlePlayerInput(self, input):
        self.cg.handlePlayerInput(input)


    def initWorldItems(self):
        for i in self.cg.getInitWorldItems():
            self.sig_addItem.emit(i)


    def get_gameTimeStamp(self):
        return time.time() - self.gameTimeStart


    def __getstate__(self):
        state = self.__dict__.copy()
        # Don't pickle vlm
        # del state["vlm"]
        return state
    

    def __setstate__(self, state):
        self.__dict__.update(state)

    