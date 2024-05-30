from game.world.worldObject import WorldObject

class Creature(WorldObject):
    
    def __init__(self, pos):
        super().__init__(pos)
        self.energy = 100.0
        self.health = 100.0
        
        
    def _updateObjectSpecificBehaviour(self):
        self.calcEnergyUsage()
    
    
    def _calcResultingForces(self):
        # TODO: Berechne Forces aus Verhalten
        pass
    
    
    def calcEnergyUsage(self):
        self.energy *= 0.999