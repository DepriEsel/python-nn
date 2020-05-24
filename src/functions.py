from math import pow, e

def sigmoid(x):
    return 1 / (1 + pow(e, -x))


def approximate(x, y, A = 1, step = 0.1, margin = 0.1, breakpoint = 100):
    loops = 0
    while True:
        E = y - (x * A)
        Eabs = abs(E)
        if(Eabs <= margin):
            break
        if(E > 0):
            A += step
        else:
            A -= step
        loops += 1
        if(loops >= breakpoint):
            print('Breakpoint reached')
            break
    return A

def approximate2(x, y, A = 1, L = 1, margin = 0.1, breakpoint = 100):
    loops = 0
    while True:
        E = y - (x * A)
        # print('E', E)
        Eabs = abs(E)
        if(Eabs <= margin):
            break
        deltaA = L * (E / x)
        # print('deltaA', deltaA)
        A += deltaA
        # print('A', A)
        loops += 1
        if(loops >= breakpoint):
            print('Breakpoint reached')
            break
    return A