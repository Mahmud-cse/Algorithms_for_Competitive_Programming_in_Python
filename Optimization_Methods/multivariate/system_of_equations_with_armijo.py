
"""
We try to solve the system of equations: Ax = b
we introduce f(x) = np.linalg.norm(Ax - b)**2
and we look for a minimum of that function 
with any method we want (in this implementation: armijo + momentum)
minimum is unique because of strict convexity of f
if the minimum is not close to zero, there is not solution to the equations

we know the gradient of f, so we do not 
need to do some numerical approx.
"""

import numpy as np

def inequality(f, C, alpha, x, fx, gradfx, direction):
	return fx + alpha * C * np.dot(gradfx, direction) - f(x + alpha * direction )


def armijo_with_momentum(f, gradf, n, tol, beta, C, eta, xi, max_iter = 1000):
	x = np.array([0]*n)
	fx = f(x)
	gradfx = gradf(x, fx)
	direction = -gradfx
	step = 0

	while fx >= tol*tol*tol:
		alpha = beta

		#compute new direction
		direction = eta * (-gradfx) + xi * direction

		while inequality(f, C, alpha, x, fx, gradfx, direction) < 0:
			alpha *= beta

		while inequality(f, C, alpha/beta, x, fx, gradfx, direction) > 0:
			alpha /= beta

		#precompute for next iteration
		x = x + alpha * direction
		fx = f(x)
		gradfx = gradf(x, fx)
		step += 1

	return x, step

def solve_system_equations(A, b, tol, beta, C, eta, xi, max_iter = 200000):
    A = np.array(A)
    b = np.array(b)
    n = A.shape[1]

    def f(x):
        return np.linalg.norm(np.dot(A, x) - b)**2

    def gradf(x, fx):
        return 2* np.dot(np.transpose(A), np.dot(A, x) - b)

    return armijo_with_momentum(f, gradf, n, tol, beta, C, eta, xi, max_iter)

#####################################
#sample input
A = [[0.99, 0.87, 0.51, 0.27], [0.34, 0.22, 0.28, 0.34], [0.86, 0.16, 0.14, 0.76], [0.74, 0.36, 0.34, 0.67]]
b = [0.22, 0.56, 0.12, 0.32]
tol = 0.001
#######################################


######################################
#hyperparameters
#armijo
beta = 1/3
C = 0.1
#momentum
eta = 0.8
xi = 0.9
######################################

mini, step = solve_system_equations(A, b, tol, beta, C, eta, xi, max_iter = 200000)
print(" ".join([str(x) for x in mini]))
print(f"The number of steps is: {step}")

