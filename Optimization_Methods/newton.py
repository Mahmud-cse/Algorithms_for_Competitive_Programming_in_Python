"""
Find minimum of function f on [a,b] with Newton method:

	We apply the Newton method, normally used to find the root
	of a function
	We apply it to f', because f'(x) = 0 at the minimum point
	We start the Newton algo at the midpoint (a+b)/2

Side Note:
We use numerical approx of f' and f'' in this implementation
"""

def d(x):
	"""
	approximate the derivate of f
	"""
	return (f(x + tol) - f(x - tol)) / (2 * tol)

def d2(x):
	"""
	approximate the second derivate of f
	"""
	return (d(x + tol) - d(x - tol)) / (2 * tol)

def newton_helper(f, df, a, tol):
	"""
	df is the derivate of f
	a is just a starting point. Pick it close to the root you want
	and we need f'(a) != 0 
	algo: we create a sequence x_0, x_1, ...x_n, starting
	with x_0 = a and x_n converges to the root.
	In this implementation, at each step we just need 
	to store the last element x_n as the point a 
	"""
	fa = f(a)

	while abs(fa) > tol:	
		slope = df(a)
		if slope == 0:
			break
		b = a - fa / slope
		# now a moves to b
		a = b
		fa = f(a)

	return a

def find_minimum(f, a, b, tol):
	"""
	output: minimum (x- coordinate) of a function f on [a,b]
	with tolerance tol

	We apply the Newton method, normally used to find the root
	of a function
	We apply it to f', because f'(x) = 0 at the minimum point
	We start the Newton algo at the midpoint (a+b)/2
	"""
	return newton_helper(d, d2, (a + b) / 2, tol)

#example use
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
#we need to pick a point in the middle here
#to be close of the root we want
res = find_minimum(f, a, b, tol)
print(res)