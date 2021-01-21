"""
This Nesterov implementation is fast:
just 300 steps for both test functions I think.
And it achieves a very good precision, 
better than the tolerance actually
#from Strang video
https://youtu.be/wrEcHhoJxjM?t=2623

what he calls "s" and "beta", we call it "alpha" and "xi"
and what Alex calls "eta" in the class is set to 1 by Strang


"""
from random import randint
from math import inf
import numpy as np

def gradf(x, f, epsilon, fx = None):
	if not fx:
		fx = f(x)
	n = len(initial)
	#we compute the matrix Epsilon, each line i is the vector (0,...,0 , epsilon, 0....,0)
	Epsilon = np.eye(n)* epsilon
	return np.array([(f(x + Epsilon[i]) - fx)/ epsilon for i in range(n)])


def nesterov(f, tol, alpha, eta, xi, max_iter = 10000):
	x1 = np.array(initial)
	n = len(initial)
	y1 = x1
	step = 0
	best_direction = 0
 

	
	# while np.linalg.norm(grady0)**2 > tol*tol*tol:
	while step <= max_iter:

		x0, y0 = x1, y1
		grady0 = gradf(y0, f, tol*tol)

		x1 = y0 - alpha * eta* grady0
		y1 = x1 + xi * (x1 - x0)
		step += 1

	return x0

################
# Sample1
def f(x): 
    n = len(x)
    p = 4
    return sum((x[i] - p)**2 for i in range(n))
tol = 0.00001
initial = (0.,) * 20 + (5.,) * 20
################
################
# Sample2
def f(x): 
    n = len(x)
    p = 1
    q = 10
    t = sum((p-x[2*i])**2+q*(x[2*i+1]-x[2*i]**2)**2 for i in range(n//2))
    return t if n % 2 == 0 else (t + x[n-1]**2)
tol = 0.00001
initial = (0.,) * 40
################


alpha = 0.01
xi = 0.9
eta = 0.8
mini  = nesterov(f, tol, alpha, eta, xi, 1000)
print(" ".join([str(x) for x in mini]))



