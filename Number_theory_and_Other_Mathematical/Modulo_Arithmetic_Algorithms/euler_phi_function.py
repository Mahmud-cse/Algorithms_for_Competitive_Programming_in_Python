"""
phi(n) is the number of integers smaller than n, that are coprime with n.
ex: phi(8) = 4, and 1,3,5,7 are coprime with 8

x ^ phi(m) = 1 [m] IF x and m are coprime
"""


def phi(n):
    """returns phi(x) for all x <= n
    ie: [phi(0), phi(1), phi(2), phi(3), ....phi(n)]
    ie: [0,1,1,2,2,4,2,6....phi(n)]
    be careful we start at phi(0) = 0, which is kindof a convention
    """
    sieve = [i if i & 1 else i // 2 for i in range(n + 1)]
    for i in range(3, n + 1, 2):
        if sieve[i] == i:
            for j in range(i, n + 1, i):
                sieve[j] = (sieve[j] // i) * (i - 1)

    return sieve

#example usage:


n = 12
#we get all the phi(k) for k in {0,1,2....12}
print(phi(n))

#usually we just want the last one:
phi_n = phi(n)[-1]
print(phi_n)