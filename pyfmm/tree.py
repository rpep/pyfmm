from __future__ import absolute_import
from .particle import Particle
import numpy as np
from .helpers import *
from .indexing import *

class NeighbourTree:
    """
    NeighbourTree

    A tree class that computes the FMM using only nearest neighbours
    for the near field calculations on each particle.
    """
    def __init__(self, r, q, maxlevel=3):
        self.order = 2 # Order of the multipole expansion
        self.maxlevel = maxlevel # maximum level.
        self.p = [Particle(rp, qp) for rp, qp in zip(r, q)] # Create particle objects
        self.p.sort(key = lambda x: x.Index(maxlevel)) # Sort the particle objects by their Morton index
        self.boxes = [2**(3*i) for i in range(maxlevel+1)] # Create list of number of boxes in the level
        self.n = sum(self.boxes)
        self.level_offsets = [0]
        a = 0
        for c, i in enumerate(self.boxes):
            a += i
            self.level_offsets.append(a)
        self.M = np.zeros((self.n, 10))
        self.L = np.zeros_like(self.M)

    @property
    def MortonIndices(self):
        """
        Returns the Morton Index of the particles.
        """
        return [part.Index(self.maxlevel) for part in self.p]

    def _getdr(self, r, I):
        """
        compute the distance from some vector
        r to that of cell I
        """
        return r - CellCoordFromIndex(I, self.maxlevel)

    def _getr(self, I, l):
        return CellCoordFromIndex(I, l)
    
    def _P2M(self):
        for p in self.p:
            I = p.Index(self.maxlevel)
            dx, dy, dz = self._getdr(p.r, I)
            cellIndex = p.Index(self.maxlevel) + self.level_offsets[self.order]
            self.M[cellIndex, 0] += p.q
            self.M[cellIndex, 1] += p.q*dx
            self.M[cellIndex, 2] += p.q*dy
            self.M[cellIndex, 3] += p.q*dz
            self.M[cellIndex, 4] += p.q*dx*dx*0.5
            self.M[cellIndex, 5] += p.q*dy*dy*0.5
            self.M[cellIndex, 6] += p.q*dz*dz*0.5
            self.M[cellIndex, 7] += p.q*dx*dy*0.5
            self.M[cellIndex, 8] += p.q*dy*dz*0.5
            self.M[cellIndex, 9] += p.q*dx*dz*0.5

    def _M2M(self):
        # Iterate through the levels
        for l in range(self.maxlevel-1,-1, -1):
            #print('Calculating M2M of level {}'.format(l))
            # Iterate through boxes in level
            for Ip in range(self.boxes[l]):
                Ic = Ip*8 + np.arange(8)
                
                Mc = Ic + self.level_offsets[l+1] # index with offset of children
                Mp = Ip + self.level_offsets[l] # index with offset
                #print('Parent index = {}, children = {}'.format(Ip, Ic))
                #print('OParent index = {}, Ochildren = {}'.format(Mp, Mc))
                rp = self._getr(Ip, l) # Coordinates of the parent
                for i in range(8): # Iterate through children
                    rc = self._getr(Ic[i], l+1)
                    dx, dy, dz = rc - rp
                    self.M[Mp, 0] += self.M[Mc[i], 0] # M_p
                    self.M[Mp, 1] += self.M[Mc[i], 1] + self.M[Mc[i], 0]*dx # D_px
                    self.M[Mp, 2] += self.M[Mc[i], 2] + self.M[Mc[i], 0]*dy # D_py
                    self.M[Mp, 3] += self.M[Mc[i], 3] + self.M[Mc[i], 0]*dz # D_pz
                    self.M[Mp, 4] += self.M[Mc[i], 4] + dz*self.M[Mc[i], 1] + 0.5*self.M[Mc[i], 0]*dx**2 # Q_pxx
                    self.M[Mp, 5] += self.M[Mc[i], 5] + dz*self.M[Mc[i], 2] + 0.5*self.M[Mc[i], 0]*dy**2 # Q_pyy
                    self.M[Mp, 6] += self.M[Mc[i], 6] + dz*self.M[Mc[i], 3] + 0.5*self.M[Mc[i], 0]*dz**2 # Q_pzz
                    self.M[Mp, 7] += self.M[Mc[i], 7] + 0.5*dx*self.M[Mc[i], 2] + 0.5*dy*self.M[Mc[i],1] + 0.5*dx*dy*self.M[Mc[i], 0] # Q_pxy
                    self.M[Mp, 8] += self.M[Mc[i], 8] + 0.5*dy*self.M[Mc[i], 3] + 0.5*dz*self.M[Mc[i],2] + 0.5*dy*dz*self.M[Mc[i], 0]# Q_pyz
                    self.M[Mp, 9] += self.M[Mc[i], 9] + 0.5*dz*self.M[Mc[i], 1] + 0.5*dx*self.M[Mc[i],3] + 0.5*dx*dz*self.M[Mc[i], 0]# Q_pxz
# parent.multipole[7:] += 0.5*numpy.array((child.multipole[2], child.multipole[3], child.multipole[1])) * numpy.array((dx, dy, dz))\
#                                 + 0.5*child.multipole[1:4] * numpy.array((dy, dz, dx))\
#                                 + 0.5*child.multipole[0] * numpy.array((dx*dy, dy*dz, dz*dx))

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

    