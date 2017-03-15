import numpy as np
import pytest
import hypothesis.strategies as st
from hypothesis import given
from particle import *

def test_create_particle():
    r = [0.4, 0.4, 0.4]
    q = 1
    p = Particle(r, q)


def test_create_particle_check_Morton_Indexing():
    r = [0.4, 0.4, 0.4]
    q = 1
    p = Particle(r, q)
    assert p.Index(0) == 0
    assert p.Index(1) == 0
    assert p.Index(2) == 7   