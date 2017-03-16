def CellFromCoord(r, l):
    """
    Cell(r, l)

    This function takes the position of a particle
    and returns the Cell indices corresponding to a
    3-D grid.

    e.g.

        +----+----+
        | X  |    |
    1   |    |    |
        +----+----+
        |    |    |
    0   |    |    |
        +----+----+
          0    +  1

    would be [0, 1, 0]

    """
    assert isinstance(l, int), "l must be an integer."
    n = 1 << l
    return [int(r[0] * n), int(r[1] * n), int(r[2] * n)]


def IndexFromCell(X, l):
    """ 
    IndexFromCell(X l)

    This function returns the Morton Index
    given the cell indices.
    """
    assert isinstance(l, int), "l must be an integer"
    assert len(X) == 3, "X must be a length three array of integers"
    for i in X:
        assert i == int(i), "X must be a length three array of integers"

    I  = 0
    for i in range(l):
        I += (X[2] & 1) << (3*i)
        I += (X[1] & 1) << (3*i + 1)
        I += (X[0] & 1) << (3*i + 2)
        X = [X[i] >> 1 for i in range(3)]
    return I


def IndexFromCoord(r, l):
    """
    Returns the Morton index 
    from the coordinates of the particle.
    """
    X = CellFromCoord(r, l)
    return IndexFromCell(X, l)


def CellFromIndex(I):
    if I != int(I):
        raise ValueError("I must be an integer")
    l = 0
    x = y = z = 0
    while(I > 0):
        z += (I & 1) << l
        I >>= 1
        y += (I & 1) << l
        I >>= 1
        x += (I & 1) << l
        I >>= 1
        l += 1
    return (x, y, z)

