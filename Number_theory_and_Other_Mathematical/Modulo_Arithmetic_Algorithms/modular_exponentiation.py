"""
algorithm is O(log n)

"""


def mod(x, n, m):
	"""
	returns x^n[m]
			| 1 if n ==0
	x^n =   | x^(n//2) * x^(n//2) if n is even
	        | x * x^(n - 1) if n is odd
	        
	When n is even, it is important to only calculate x^(n//2) once to keep the 
	time complexity at O(log n)
	"""
    if n == 0:
        return 1
    elif n == 1:
        return x % m
    else:
        result = mod(x, n//2, m)
        if n % 2:
            return result * result * x % m
        else:
            return result * result % m

