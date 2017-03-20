from hypothesis import given
import hypothesis.strategies as st
from pyfmm import *
import numpy.testing as npt

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


def test_I_example_1():
    l = 3
    r = [0.4, 0.4, 0.4]
    q = 1
    assert IndexFromCoord(r, 0) == 0
    assert IndexFromCoord(r, 1) == 0
    assert IndexFromCoord(r, 2) == 7


def test_IndexFromCell():
    l = 0
    X = [0, 0, 0]
    assert IndexFromCell(X, l) == 0


def CellCoordFromIndex(I, l):
    """
    Returns the coordinate of the centre of a cell given by 
    Morton Index I at level l
    """
    nx = 2**l
    return 1.0/nx*np.array(CellFromIndex(I))+1/(2.0*nx)*np.ones(3)

def CellCoordFromCell(X, l):
    """
    Returns the coordinate of the centre of a cell given 
    by the index at level l.
    """
    nx = 2**l
    return 1.0/nx*np.array(X)+1/(2.0*nx)*np.ones(3)


def test_CellCoordFromIndex():
    l = 0
    I = 0
    CellCoordFromIndex(0, 0) == np.array([0.5, 0.5, 0.5])
    npt.assert_array_equal(CellCoordFromIndex(0, 0), np.array([0.5, 0.5, 0.5]))

def test_CellFromIndex():
    assert CellFromIndex(0) == (0,0,0)
    assert CellFromIndex(1) == (1,0,0)
    assert CellFromIndex(2) == (0,1,0)
    assert CellFromIndex(3) == (1,1,0)
    assert CellFromIndex(4) == (0,0,1)
    assert CellFromIndex(5) == (1,0,1)
    assert CellFromIndex(6) == (0,1,1)
    assert CellFromIndex(7) == (1,1,1)
    assert CellFromIndex(8) == (2,0,0)
    assert CellFromIndex(9) == (3,0,0)
    assert CellFromIndex(10) == (2,1,0)
    assert CellFromIndex(11) == (3,1,0)
    assert CellFromIndex(12) == (2,0,1)
    assert CellFromIndex(13) == (3,0,1)
    assert CellFromIndex(14) == (2,1,1)
