import time

from PyQt5.Qt import QPen, QColor
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsTextItem

class Interaction():
    
    def __init__(self, name, reactime, pos, size=[50,50]):
        
        self.name = name
        self.endtime = time.time() + reactime
        
        self.pos = pos
        self.size = size
        
        self.alive = True
        
        self.item = InteractionItem(self)
        
        
    def update(self):
        if(time.time() > self.endtime):
            self.alive = False



class InteractionItem(QGraphicsRectItem):
    
    def __init__(self, interaction: Interaction):
        
        super().__init__()
        self.i = interaction
        
        self.setRect(self.i.pos[0], self.i.pos[1], self.i.size[0], self.i.size[1])
        self.setPen(QPen(QColor.fromRgb(255,255,255)))
        
        self.text = QGraphicsTextItem("", self)
        self.text.setTextWidth(self.boundingRect().width())
        self.text.setHtml('<center style="color:white">' + self.i.name +'</center>')
        rect = self.text.boundingRect()
        rect.moveCenter(self.boundingRect().center())
        self.text.setPos(rect.topLeft())
        
        
        
        