"""
Methods to find the root of a function:
1/Bisection (alpha = 1)
2/Secant (alpha = 1,618...)
3/Newton (alpha = 2)
alpha bigger iff convergence is faster
So why not always use the fastest one?
BECAUSE:
-Newton needs derivative, sometimes we dont want/have it
-Newton and secant are not guaranteed to converge, Bisection method is
So we need to know the 3 methods

In all those algos, we add a max_iter condition to be sure we avoid
infinite loop and to control the time of execution

If you are using Newton or secant method
trying to find a root in a specific interval
a good idea is to plot the function on WolframAlpha
to chose a good starting point for the algorithm

for example, in the testcase below, we
apply newton to the midpoint of the interval
and i believe applying to the extremities wouldnt work
"""

from math import inf
def bisection(f, a, b, tol, max_iter = 1000):
	"""
	find the root of a function on a segment [a,b]
	if it exists inside the segment
	and if f(a) and f(b) have different signs
	"""
	low = a
	high = b

	assert f(a)*f(b) < 0

	if f(a) > 0:
		sign_left = 1
	else:
		sign_left = -1

	if (b-a) <= tol:
		return (a + b)/2
	step = 0
	while (high - low) > tol*tol and step < max_iter:
		step += 1
		mid = (low + high) / 2
		#we save this val to just do one function call
		#instead of two
		val = f(mid)
		if val == 0:
			break
		elif val*sign_left > 0:
			low = mid
		else:
			high = mid

	return mid

def secant(f, a, b, tol, max_iter = 1000):
	"""
	a and b are just the 2 starting points. The root doesnt have to be inside 
	the segment [a,b]
	BUT: need to pick a and b such as f(a) != f(b)

	algo: we create a sequence x0, x1, ...xn, starting
	with x0 = a and x1 =b, xn converges to the root.
	In this implementation, at each step we just need 
	to store the last 2 elements that we call a and b
	"""
	fa = f(a)
	fb = f(b)
	assert fa != fb
	step = 0
	while abs(b-a) > tol*tol and step < max_iter:
		step += 1	
		if a == b:
			break
		slope = (fb - fa) / (b - a)
		if slope == 0:
			break
		c = b - fb /slope
		fc = f(c)
		# now a moves to b and b moves to c
		a, fa, b, fb = b, fb, c, fc

	return b


def df(x, epsilon):
	"""
	approximate the derivate of f
	we could also put here the exact symbolic 
	when it is easy to calculate 
	(here the derivate is just f'(x) = 2*x 
	but it could be a very complicated function)
	"""
	return (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)


def newton(f, df, a, tol, max_iter = 1000):
	"""
	df is the derivate of f (can be simple numerical approximation)
	a is just a starting point. Pick it close to the root you want
	and we need f'(a) != 0 

	algo: we create a sequence x_0, x_1, ...x_n, starting
	with x_0 = a and xn converges to the root.
	In this implementation, at each step we just need 
	to store the last element x_n as the point a
	"""
	fa = f(a)
	move = inf # just to avoid triggerrig the initial while loop
	step = 0
	while abs(move) > tol*tol and step < max_iter:
		step += 1
		slope = df(a, tol*tol)
		if slope == 0:
			break
		move  = - fa /slope
		a = a + move
		fa = f(a)

	return a

#example testcase
################################
from math import sqrt, sin
a = .01
b = 1.
tol = 0.00001
f = lambda x: sqrt(x)-2*sin(x)
################################



max_iter = 1000
print(secant(f, a, b, tol, max_iter))
print(bisection(f, a, b, tol, max_iter))
print(newton(f, df, (a + b)/ 2, tol, max_iter))
	

