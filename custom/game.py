from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QGraphicsItem

from custom.player import CustomPlayer
from custom.interaction import Interaction


class CustomGame(QObject):

    sig_addItem = pyqtSignal(QGraphicsItem)
    sig_removeItem = pyqtSignal(QGraphicsItem)
    
    def __init__(self, wrapperGame):
        super().__init__()
      
        self.g = wrapperGame
        self.p = CustomPlayer()
        
        self.interactions = []
        

##################
# Template Methods

    def updateGame(self):
        self.p.me.calcUpdateChanges()
        
        # Interactions
        self.generateInteractions()
        for i in self.interactions:
            i.update()
        self.removeDeadInteractions()
        
    
    
    def generateInteractions(self):
        if(len(self.interactions) == 0 and self.g.gameTime < 1):
            i = Interaction(name="Test", reactime=5, pos=[200,200], size=[100,50])
            self.interactions.append(i)
            self.sig_addItem.emit(i.item)
    
    
    def removeDeadInteractions(self):
        for i in reversed(self.interactions):
            if (not i.alive):
                self.sig_removeItem.emit(i.item)
                self.interactions.remove(i)
        
        
    def getInitWorldItems(self):
        return [self.p.getInitItems()]
        

    def handlePlayerInput(self, input):
        self.cg.handlePlayerInput(input)
        
        
    def getQuickStats(self):
        return {"pos": str(self.p.me.pos), "energy": f"{self.p.me.energy:.2f}"}