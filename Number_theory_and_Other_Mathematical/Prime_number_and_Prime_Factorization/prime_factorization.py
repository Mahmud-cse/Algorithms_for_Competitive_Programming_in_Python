"""
Note: sometimes if you just need the number of prime factors of n, or the largest prime factor of n, but for many testcases, it is more efficient to precompute it for all numbers
It might seem like it is slow to precompute (takes like 10s), but it passes tests in Pypy
"""


def precompute(N = 2*10**7):
    """Precompute 2 lists
            - number of distinct prime factors (for each x in [1,N])
            - largest prime factor             (for each x in [1,N]) 
    """
    N += 1 
    print("Precomputing for 8s...")
    n = 2 * 10 ** 7 + 1
    primeCount = [0] * N
    largestPrime = [-1] * N
    for p in range(2, N):
        if largestPrime[p] == -1:
            for m in range(p, N, p):
                largestPrime[m] = p
                primeCount[m] += 1
    return primeCount, largestPrime


def divisors(n):
    front = []
    back = []
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            front.append(x)
            back.append(n // x)
    #check for the last one added, if x == n//x, dont want to add it twice in the list of divisors
    if front[-1] == back[-1]:
        front.pop()
    return front + back[::-1]



def factorize(n):
    """
    returns [(p1, k1), (p2, k2), ...]
    if n == 1, it returns []

    """
    fct = []
    
    for i in range(2, int(n**0.5)+1):
        c = 0
        
        while n%i==0:
            n //= i
            c += 1
            
        if c>0:
            fct.append((i, c))
    
    if n>1:
        fct.append((n, 1))
    
    return fct





#driving code
n = 56
print(f"What are all the divisors of {n}? ", divisors(n))
print(f"What is the prime factorization of {n}? ", factorize(n))

primeCount, largestPrime = precompute()
print(f"What is the biggest prime number dividing {n}? ", largestPrime[56])
print(f"How prime numbers divide {n}? ", primeCount[56])