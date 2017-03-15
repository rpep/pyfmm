import numpy as np
import pytest
import hypothesis.strategies as st
from hypothesis import given
from particle import *

@given(st.lists('float', min_length=3, max_length=3), st.floats())
def test_create_particle(r, q):
    p = Particle(r, q)
