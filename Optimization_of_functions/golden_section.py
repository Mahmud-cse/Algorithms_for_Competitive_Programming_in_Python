"""
Assuming we are given a function f, 
that is unimodal(only one minumum on [a,b])
we can use this algorithm to find the min

Note that the algo is written such that there is only one 
call to f per iteration of the while loop (thanks to golden ratio)
"""
from math import sqrt

def golden_section(f, a, b, tol):
    alpha  = (3 - sqrt(5)) / 2

    c = (1 - alpha) * a + alpha * b
    d = alpha * a + (1 - alpha) * b
    fa = f(a)
    fb = f(b)
    fc = f(c)
    fd = f(d)

    while (b - a) > tol:
        if fc < fd:
            # b moves to d and c becomes the new d on [a, b = old_d]
            b = d
            fb = fd
            d = c
            fd = fc

            c = (1 - alpha) * a + alpha * b
            fc  = f(c)
        else:
            a = c
            fa = fc
            c = d
            fc = fd
            d = alpha * a + (1 - alpha) * b
            fd = f(d)
    return a




