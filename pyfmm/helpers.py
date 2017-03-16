import itertools

def unique_permutations(l):
    combo = [0, 1, 2]
    test = [sorted(list(i)) for i in list(itertools.product(*[combo for j in range(l)]))]
    a = []
    for j in test:
        if j not in a:
            a.append(j)
    return a