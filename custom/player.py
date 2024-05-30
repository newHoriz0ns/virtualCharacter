from game.player import Player
from game.world.life.human import Human

from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage

class CustomPlayer(Player):
    
    def __init__(self):
        super().__init__()
        self.me = Human(pos = [0,0,0])
        self.me.item = ItemPlayer(self)
        
        
        
    def getInitItems(self):
        return self.me.item
        
        
            
        
    
    
    
    
class ItemPlayer(QGraphicsPixmapItem):
    
    def __init__(self, player: CustomPlayer):
        super().__init__()
        self.imgHuman = QImage("gfx/game/player.png")
        self.setPixmap(QPixmap.fromImage(self.imgHuman))
        self.p = player
        
        
        
    