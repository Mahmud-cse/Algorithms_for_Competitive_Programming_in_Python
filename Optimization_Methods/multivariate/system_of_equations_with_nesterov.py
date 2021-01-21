"""
Nesterov to solve system of equations

Interesting to notice a nice linear algebra 
formula for the gradient of f.
"""

import numpy as np
from math import inf

def nesterov(f, gradf, n, alpha, eta, xi, max_iter = 10000):
    x0 = inf #to enter the while loop
    x1 = np.array([0]*n)
    y1 = x1
    step = 0
 
    while np.linalg.norm(x0 - x1) > tol**3 and step <= max_iter:

        x0, y0 = x1, y1
        grady0 = gradf(y0, f)

        x1 = y0 - alpha * eta* grady0
        y1 = x1 + xi * (x1 - x0)
        step += 1

    return x0, step

#####################
#test case
A = [[0.99, 0.87, 0.51, 0.27], [0.34, 0.22, 0.28, 0.34], [0.86, 0.16, 0.14, 0.76], [0.74, 0.36, 0.34, 0.67]]
b = [0.22, 0.56, 0.12, 0.32]
tol = 0.001
#####################

def solve_system_equations(A, b, tol, alpha, eta , xi, max_iter = 200000):
    A = np.array(A)
    b = np.array(b)
    n = A.shape[1]

    def f(x):
        return np.linalg.norm(np.dot(A, x) - b)**2

    def gradf(x, fx):
        return 2* np.dot(np.transpose(A), np.dot(A, x) - b)

    return nesterov(f, gradf, n, alpha, eta, xi, max_iter)


#hyperparameters
alpha = 0.01
xi = 0.9
eta = 0.8

mini, step = solve_system_equations(A, b, tol, alpha, eta , xi, max_iter = 200000)
print(" ".join([str(x) for x in mini]))
print(step)