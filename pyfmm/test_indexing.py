from hypothesis import given
from indexing import *
import hypothesis.strategies as st

@given(st.integers(0, 7))
def test_I_l1(I):
    l = 1
    nx = 1 << l
    cells = CellFromIndex(I)
    try:
        # Check that the cells ranges are correct
        for i in cells:
            assert i < nx
            assert i >= 0
        # Check the back conversion gives the same thing.
        assert I == IndexFromCell(CellFromIndex(I), l)
        
    except AssertionError:
    	print('Cells = {}, I = {}'.format(cells, I))
    	raise AssertionError

@given(st.integers(0, 63))
def test_I_l2(I):
    l = 2
    nx = 1 << l
    cells = CellFromIndex(I)
    try:
        # Check that the cells ranges are correct
        for i in cells:
            assert i < nx
            assert i >= 0
        # Check the back conversion gives the same thing.
        assert I == IndexFromCell(CellFromIndex(I), l)

    except AssertionError:
    	print('Cells = {}, I = {}'.format(cells, I))
    	raise AssertionError


@given(st.integers(0, 511))
def test_I_l3(I):
    l = 3
    nx = 1 << l
    cells = CellFromIndex(I)
    try:
        # Check that the cells ranges are correct
        for i in cells:
            assert i < nx
            assert i >= 0
        # Check the back conversion gives the same thing.
        assert I == IndexFromCell(CellFromIndex(I), l)
        
    except AssertionError:
    	print('Cells = {}, I = {}'.format(cells, I))
    	raise AssertionError


@given(st.integers(0, 4095))
def test_I_l4(I):
    l = 4
    nx = 1 << l
    cells = CellFromIndex(I)
    try:
        # Check that the cells ranges are correct
        for i in cells:
            assert i < nx
            assert i >= 0
        # Check the back conversion gives the same thing.
        assert I == IndexFromCell(CellFromIndex(I), l)
        
    except AssertionError:
    	print('Cells = {}, I = {}'.format(cells, I))
    	raise AssertionError