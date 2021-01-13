

def d(x):
	"""
	approximate the derivate of f
	"""
	return (f(x + tol) - f(x - tol)) / (2*tol)

def d2(x):
	"""
	approximate the second derivate of f
	"""
	return (d(x + tol) - d(x - tol)) / (2*tol)

def newton(f, g, a, tol):
	"""
	g is just the derivate of f
	a is just a starting point. Pick it close to the root you want
	and we need f'(a) != 0 
	algo: we create a sequence x0, x1, ...xn, starting
	with x0 = a and xn converges to the root.
	In this implementation, at each step we just need 
	to store the last element that we call a
	"""
	fa = f(a)

	while abs(fa) > tol:	
		rope = g(a)
		if rope == 0:
			break
		b = a - fa /rope
		# now a moves to b
		a = b
		fa = f(a)

	return a

#example use
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
#we need to pick a point in the middle here
#to be close of the root we want
res = newton(d, d2, (a + b) / 2, tol)
print(res)