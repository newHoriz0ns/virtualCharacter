
import time

from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsScene, QLineEdit, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from mainFrame.graphicsViewGame import WeltGraphicsViewWidget
from mainFrame.graphicsViewStats import StatsGraphicsViewWidget


from mainFrame.screen import Screen
from game.game import Game

class ScreenPlay(Screen):

    _sig_pause = pyqtSignal()

    def __init__(self, mainWindow):

        super().__init__(mainWindow)
        
        #####
        # Game
        
        self.game = None
        
        
        ##############
        # Left Menü
        
        self.menuGroup = QGroupBox()
        self.menuLayout = QVBoxLayout()
        self.menuGroup.setLayout(self.menuLayout)
        self.menuGroup.setFixedWidth(250)
        self.mainLayout.addWidget(self.menuGroup)
        
        # Pause Game
        self.pbPause = QPushButton("Pause")
        self.menuLayout.addWidget(self.pbPause)
        self.pbPause.clicked.connect(self.on_PauseClicked)


        ##############
        # Center (Game)
        
        self.groupGame = QGroupBox()
        self.layoutGame = QVBoxLayout()
        self.groupGame.setLayout(self.layoutGame)
        self.mainLayout.addWidget(self.groupGame)
        
        # Welt
        self.weltView = WeltGraphicsViewWidget()
        self.layoutGame.addWidget(self.weltView)
        
        # Bottom (Status & QuickItems)
        self.statsView = StatsGraphicsViewWidget(10)
        self.layoutGame.addWidget(self.statsView)


        ###############
        # Right Menu ?
        
        
    def on_PauseClicked(self):
        self._sig_pause.emit()
        
        
    
    def startGame(self):
        self.game = Game()
        self.weltView.setGame(self.game)
        self.statsView.setGame(self.game)
        
        # Add and Remove Items
        self.game.sig_addItem.connect(self.weltView.addItem)
        self.game.sig_removeItem.connect(self.weltView.removeItem)
        
        # React on Updates
        self.game.sig_gameUpdate.connect(self.statsView.update)
        
        # Load items at start of game
        self.game.initWorldItems()
    
    
    
    
    def loadGame(self, sav):
        # TODO: Load Game
        pass
        
        
        
        
        
    def updateView (self):
        # WeltView
        self.weltView.update_graphicsView()
        # Stats
        self.statsView.update()

        if(self.game != None):
            self.game.update()


    def saveModel(self):
        # modelio.saveModelToFile(self.m, "sav/test.sav")
        pass
    
    def loadModel(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "sav/","All Files (*);; Save Files (*.sav)", options=options)
        if fileName:
            # self.m = modelio.loadModelFromFile(fileName)
            pass

    def setPlayerName(self, name):
        self.m.getPlayer().name = name


    def setPlayerEnergie(self, energie):
        self.m.getPlayer().energie = float(energie)
        
    