from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QGraphicsItem

from custom.player import CustomPlayer



class CustomGame(QObject):

    sig_addItem = pyqtSignal(QGraphicsItem)
    sig_removeItem = pyqtSignal(QGraphicsItem)
    
    def __init__(self):
        super().__init__()
      
        self.p = CustomPlayer()
        
    

##################
# Template Methods

    def updateGame(self):
        self.p.me.calcUpdateChanges()
        
        
    def getInitWorldItems(self):
        return [self.p.getInitItems()]
        

    def handlePlayerInput(self, input):
        self.cg.handlePlayerInput(input)
        
        
    def getQuickStats(self):
        return {"pos": str(self.p.me.pos), "energy": f"{self.p.me.energy:.2f}"}