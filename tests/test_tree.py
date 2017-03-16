from hypothesis import given
import numpy as np
import hypothesis.strategies as st
from hypothesis.extra.numpy import arrays
from pyfmm import *

def test_create_NeighbourTree():
	r = np.random.uniform(0, 1, (100, 3))
	q = np.random.uniform(-1, 1, 100)
	n = NeighbourTree(r, q)


def test_Neighbour_Tree_Sorted_Correctly():
    r = np.random.uniform(0, 1, (100, 3))
    q = np.random.uniform(-1, 1, 100)
    n = NeighbourTree(r, q, maxlevel=3)
    if sorted(n.MortonIndices) != n.MortonIndices:
    	raise AssertionError("Morton Indices are not sorted in tree")


def test_Neighbour_Tree_Offsets_Correct():
    r = np.random.uniform(0, 1, (100, 3))
    q = np.random.uniform(-1, 1, 100)
    n = NeighbourTree(r, q, maxlevel=2)
    assert n.level_offsets == [0, 1, 9]
    n = NeighbourTree(r, q, maxlevel=3)
    assert n.level_offsets == [0, 1, 9, 73]
    n = NeighbourTree(r, q, maxlevel=4)
    assert n.level_offsets == [0, 1, 9, 73, 585]
    n = NeighbourTree(r, q, maxlevel=5)
    assert n.level_offsets == [0, 1, 9, 73, 585, 4681]

