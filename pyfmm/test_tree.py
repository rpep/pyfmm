from hypothesis import given
import numpy as np
import hypothesis.strategies as st
from hypothesis.extra.numpy import arrays

@given(arrays(np.float))
def test_create_NeighbourTree(r, q):
	n = NeighbourTree(r, q)