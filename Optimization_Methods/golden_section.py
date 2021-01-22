#number of steps : about 30 steps for both testcases

"""
Assuming we are given a function f, 
that is unimodal(only one minimum on [a,b])
we can use this algorithm to find the min

Golden Search Algo:
At each step, given a and b, we want to check the value of f
at intermediary points c and d inside [a,b] (ternary search)
The choice of c and d depending on golden ratio
saves us one function call at each iteration,
because amongst the new values of c and d, either
c is actually the previous d or d is the previous c
"""

from math import sqrt

def golden_ratio(f, a, b, tol, max_iter = 1000):
    phi = (1 + sqrt(5)) / 2
    alpha  = 1 / phi
    c = alpha * a + (1 - alpha) * b
    d = (1 - alpha) * a + alpha * b
    step = 0

    fc, fd = f(c), f(d)

    while (b - a) > tol and step < max_iter:
        step += 1
        if fc < fd:
            #b moves to d, d moves to c
            b, fb, d, fd = d, fd, c, fc
            c = alpha * a + (1 - alpha) * b
            fc= f(c)
        else:
            #a moves to c, c moves to d
            a, fa, c, fc = c, fc, d, fd
            d = (1 - alpha) * a + alpha * b
            fd = f(d)
    return c, step



######################
# Sample Input 1:
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
######################

######################
# Sample Input 2:
f = lambda x: x**1.8 - 15*x + 4
a = 2.
b = 30.
tol = 0.000001
######################


mini, step = golden_ratio(f, a, b, tol, max_iter = 1000)
print(mini)
print(f"the number of steps required is {step}") #36
