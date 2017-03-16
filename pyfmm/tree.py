from __future__ import absolute_import
from .particle import Particle
import numpy as np
from .helpers import *

class NeighbourTree:
    """
    NeighbourTree

    A tree class that computes the FMM using only nearest neighbours
    for the near field calculations on each particle.
    """
    def __init__(self, r, q, maxlevel=2, order=0):
        self.order = order
        if self.order > 0:
            raise NotImplemented
        self.maxlevel = maxlevel
        self.p = [Particle(rp, qp) for rp, qp in zip(r, q)]
        self.p.sort(key = lambda x: x.Index(maxlevel))
        temp = [2**(3*i) for i in range(maxlevel)]
        self.n = sum(temp)
        self.level_offsets = [0]
        a = 0
        for c, i in enumerate(temp):
            a += i
            self.level_offsets.append(a)
        self.M = np.zeros((self.n, order+1))
        self.L = np.zeros_like(self.M)

    @property
    def MortonIndices(self):
        """
        Returns the Morton Index of the particles.
        """
        return [part.Index(self.maxlevel) for part in self.p]

    def _P2M(self):
        for p in self.particle:
            M[0, p.Cell(self.maxlevel) + self.level_offsets] += p.q


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