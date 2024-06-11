
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox , QHBoxLayout, QVBoxLayout, QLabel, QLineEdit

class StatsGraphicsViewWidget(QGroupBox):
    
    def __init__(self, statsCnt):
        super().__init__()
        self.game = None
        
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)

        # Init empty StatsItems        
        self.statsItems = {}
        for i in range(statsCnt):
            s = StatsItem(str(i))
            self.statsItems[i] = s
            self.mainLayout.addWidget(s)
            
        self.statsNameMapping = {}

        
    def setGame(self, game):
        self.game = game
        self.initStatItems()
        
        
    def initStatItems(self):
        for i, n in enumerate(self.game.getQuickStats()):
            self.statsNameMapping[n] = i
            self.statsItems[i].setLabel(n)
            
            
    def update(self):
        if(self.game != None):
            qs = self.game.getQuickStats()
            for n in qs:
                if(n in self.statsNameMapping):
                    i = self.statsNameMapping[n]
                    self.statsItems[i].setValue(str(qs[n]))
            
        
        
class StatsItem(QGroupBox):
    
    def __init__(self, name):
        super().__init__()
        
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        
        self.lName = QLabel(name)
        self.mainLayout.addWidget(self.lName)
        self.lName.setAlignment(Qt.AlignCenter)
        
        self.lValue = QLineEdit("")
        self.mainLayout.addWidget(self.lValue)
        self.lValue.setReadOnly(True)
        self.lValue.setAlignment(Qt.AlignCenter)
        
        self.setVisible(False)
        
        self.setFixedSize(100, 70)
    
    
    def setLabel(self, name):
        self.lName.setText(name)
        self.setVisible(True)
        
    def setValue(self, val: str):
        self.lValue.setText(val)