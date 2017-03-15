from indexing import *

class Particle:
    """
    Class representing a particle.
    
    x = x position
    y = y position
    z = z position
    q = charge/mass/etc.
    """
    def __init__(self, r, q):
        self.r = r
        self.q = q

    def Cell(self, l):
        return CellFromCoord(self.r, l)
    

    def Index(self, l):
        return IndexFromCoord(self.r, l)