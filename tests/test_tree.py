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

def test_Neighbour_Tree_P2M():
    r = np.random.uniform(0, 1, (100, 3))
    q = np.random.uniform(-1, 1, 100)
    n = NeighbourTree(r, q, maxlevel=3)
    n._P2M()


@given(st.integers(0, 500))
def test_P2P_M2M(N):
    r = np.random.uniform(0, 1, (N, 3))
    q = np.ones(N)
    n = NeighbourTree(r, q, maxlevel=2)
    n._P2M()
    n._M2M()
    assert sum(n.M[9:, 0]) == N
    assert n.M[0, 0] == N
