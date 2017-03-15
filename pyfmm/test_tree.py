from hypothesis import given
import numpy as np
import hypothesis.strategies as st
from hypothesis.extra.numpy import arrays
from tree import *

def test_create_NeighbourTree():
	r = np.random.uniform(0, 1, (100, 3))
	q = np.random.uniform(-1, 1, 100)
	n = NeighbourTree(r, q)