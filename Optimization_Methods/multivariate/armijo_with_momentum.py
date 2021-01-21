"""
Implementation of Armijo's rule + Momentum with numpy
It gets the result in :
-174 steps for first test case
- 7788 steps for second testcase
#############################################
If you dont want momentum, you can just set:
eta = 1
xi = 0
to get vanila Armijo
#############################################
"""

import numpy as np
from math import inf

def armijo(C, alpha, x, fx, gradfx, direction):
	return fx + alpha * C * np.dot(gradfx, direction) - f_np(x + alpha * direction )

def f_np(x):
	"""
	input: numpy vector x
	output : the value of f(x)
	this helper function is needed because the testcase fucntion
	parameters are unpacked tuples, not numpy arrays
	"""
	return f(*tuple(x))

def gradf(x, fx, epsilon):
	n = len(initial)
	Epsilon = np.eye(n) * epsilon
	return np.array([(f_np(x + Epsilon[i]) - fx)/epsilon for i in range(n)])

def optimizer(f_np, initial, tolerance, max_iter,beta, C, eta, xi):
	x = np.array(initial)
	fx = f_np(x)
	gradfx = gradf(x, fx, tol*tol)
	direction = -gradfx
	minalpha = 1

	step = 0

	while np.linalg.norm(gradfx)**2 > tol*tol*tol and step < max_iter:
		alpha = beta

		#compute new direction
		direction = eta * (-gradfx) + xi * direction
		max_iter_armijo = 100
		current_iter_armijo = 0
		while armijo(C, alpha, x, fx, gradfx, direction) < 0:
			current_iter_armijo += 1
			alpha *= beta
			if current_iter_armijo >  max_iter_armijo:
				return x, step
		while armijo(C, alpha/beta, x, fx, gradfx, direction) > 0:
			alpha /= beta

		#precompute for next iteration
		progress = alpha * direction
		x = x + alpha * direction
		fx = f_np(x)
		gradfx = gradf(x, fx, tol*tol/(step + 1))
		step += 1

	return x, step

###########################
#input1
def f(x1, x2): 
    p = 1
    q = 10
    return (p-x1)**2+q*(x2-x1**2)**2
tol = 0.00001
initial = (0., 0.)
###########################
###########################
#input2
def f(x1, x2): 
    p = 4
    q = 5
    return (p-x1)**2+q*(x2-x1**2)**2
tol = 0.00001
initial = (10., 0.)
###########################


####################################################
#hyperparameters

#armijo
beta = 1/3
C = 0.1
#momentum
eta = 0.8
xi = 0.9
####################################################

mini, step = optimizer(f_np, initial, tol, 10000,beta, C, eta, xi)
for i in range(len(mini)):
	print(mini[i], end = " ")
print()
print(f"The number of steps is: {step}") #174