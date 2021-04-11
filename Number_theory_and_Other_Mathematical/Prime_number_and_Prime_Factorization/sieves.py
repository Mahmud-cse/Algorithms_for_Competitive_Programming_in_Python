"""
there are many kind usefull precomputations grouped here
"""
from math import sqrt

def precompute_factorization_no_squares(N_MAX = 10**7 + 1):
	"""
    output: a list, such that for each n <= N_MAX, if n = p1^e1*p2^e2...pk^ek, 
    then canonical_forms[n] = pi1 * pi2 *...* pij with only the pi such as ei is odd
    
	See good explanation from neal E1: https://www.youtube.com/watch?v=WBcp1VRQGVk

	Remember the prime factorization of all numbers
	if you want to check if some products of 2 numbers is a square or not
	you can first reduce all numbers to a a canonical form which is their prime factorization
	where you only keep the primes that have odd exposant (basically you take exposant mod 2)
	example 8 becomes 2
	2^6*3^153*5^1023 becomes 3*5

	then 2 numbers product is a square iff they have the EXACT SAME canonical form
	"""
	squares = set([i*i for i in range(1, int(sqrt(N_MAX)))])
 
	canonical_forms = [i for i in range(N_MAX)]
	for i in range(1,N_MAX+1):
	    if canonical_forms[i] == i:
	        for sq in squares:
	            if i*sq > N_MAX: break
	            canonical_forms[i*sq] = i
	return canonical_forms


def precompute_count_of_prime_factors_and_the_largest_one(N = 2*10**7):
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