"""
author: Paul
version: v0.2
lastChange: 31.7.23
"""

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QCloseEvent, QKeyEvent

from PyQt5.QtWidgets import QMainWindow

import mainFrame.viewLayerManager as vlm
import mainFrame.viewContainer as vc


class MainFrame(QMainWindow):

    CONTINOUS_UPDATE = True
    
    def __init__(self):
        super().__init__()

        # Init Viel Layer Manager
        self.vlm = vlm.ViewLayerManager(self)
        

        # ViewContainer
        self.viewContainer = vc.ViewContainer()
        self.setCentralWidget(self.viewContainer)

        # Setze View in Controller 
        self.vlm.set_viewContainer(self.viewContainer)
        
        
        self.lastUpdate = 0
        
        if(self.CONTINOUS_UPDATE):
            self.init_updateRoutine()
            self.start_updateRoutine()
            
        

    def set_viewLayerManager(self, vlm):
        self.vlm = vlm



    def set_viewLayout(self, layout, structure):
        """
        Übergibt die neue Struktur an die MainView
        """
        self.view.set_layout(layout, structure)
        
        
        
    def init_updateRoutine(self):
        """
        Initialisierung durch Main
        """
        self.updateTimer = QTimer()
        self.updateTimer.setTimerType(Qt.PreciseTimer)
        self.updateTimer.setInterval(0) # Wird durch vsync gesteuert
        self.updateTimer.timeout.connect(self.vlm.update_vlm, Qt.DirectConnection)


    def start_updateRoutine(self):
        self.updateTimer.start()




    #################
    # EVENT HANDLER
    #


    def keyPressEvent(self, a0: QKeyEvent) -> None:
        self.vlm.handleKeyPress(a0)
        return super().keyPressEvent(a0)
    
    
    def keyReleaseEvent(self, a0: QKeyEvent) -> None:
        self.vlm.handleKeyRelease(a0)
        return super().keyReleaseEvent(a0)
    


    ################
    # Close Event Handler
    # 

    def closeEvent(self, a0: QCloseEvent) -> None:
        return super().closeEvent(a0)
        print("closed")