
from math import gcd


def gcd_euclid(a, b):  
    """
    actually no need it, it is in the module math
    """
    if a < b:
        return gcd(b, a)
    while b != 0:
        a, b  = b, a % b
    return a


for a in range(500):
    for b in range(500):
        assert(gcd(a,b) ==  gcd_euclid(a,b))