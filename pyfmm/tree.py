from particle import Particle

class NeighbourTree:
    """
    NeighbourTree

    A tree class that computes the FMM using only nearest neighbours
    for the near field calculations on each particle.
    """
    def __init__(self, r, q, maxlevel=3):
        self.maxlevel = maxlevel
        self.p = [Particle(rp, qp) for rp, qp in zip(r, q)]
        self.p.sort(key = lambda x: x.Index(maxlevel))
    
    @property
    def MortonIndices(self):
        """
        Returns the Morton Index of the particles.
        """
        return [part.Index(self.maxlevel) for part in self.p]

    def _P2M(self):
        pass

    def _M2L(self):
        pass

    def _L2L(self):
        pass

    def _L2P(self):
        pass

    def _P2P(self):
        pass

    def compute_potential(self):
        pass