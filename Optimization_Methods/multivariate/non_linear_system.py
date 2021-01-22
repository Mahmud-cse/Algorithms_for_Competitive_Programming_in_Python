#this implementation can solve both testcases in about 1000 steps (688 and 2353)
import numpy as np
from math import inf

def nesterov(F, grad_approx, x_init, y_init, alpha, eta, xi, max_iter = 10000):
    x0 = inf #to enter the while loop
    x1 = np.array([x_init, y_init])
    y1 = x1
    step = 0
 
    while np.linalg.norm(x0 - x1) > tol**3 and step <= max_iter:

        x0, y0 = x1, y1
        grady0, _ = grad_approx(y0, tol**2)

        x1 = y0 - alpha * eta* grady0
        y1 = x1 + xi * (x1 - x0)
        step += 1

    return x0, step


def solve(f, g, tol, x_init, y_init,alpha, eta , xi, max_iter = 200000):
    def F(x):
        return f(x[0], x[1])**2 + g(x[0], x[1])**2

    def grad_approx(x, epsilon, Fx = None):
        if not Fx:
            Fx = F(x)
        gradx1 = (F((x[0] + epsilon, x[1])) - Fx) / epsilon
        gradx2 = (F((x[0], x[1] + epsilon)) - Fx) / epsilon
        return np.array([gradx1, gradx2]), Fx

    mini, step =  nesterov(F, grad_approx,  x_init, y_init,alpha, eta, xi, max_iter)
    fmin = F(mini)
    if fmin > tol:
        print(f"minimum of f is {fmin}. It should be almost zero.")
        print(f"If it is not close to zero, the system has no solutions.")
    return fmin, mini, step

##############################
# Sample Input 1:

from math import sin, cos
tol = 0.0001
x_init = 1.0 
y_init = -1.0
f = lambda x, y: cos(x*y)-0.5
g = lambda x, y: sin(x+y)-0.3
##############################

##############################
# Sample Input 2:

# from math import exp, cos
# tol = 0.0001
# x_init = -3.0 
# y_init = 3.0
# f = lambda x, y: exp(x) - cos(y)
# g = lambda x, y: x + y + exp(x+y) - 10
##############################

#hyperparameters
alpha = 0.001
xi = 0.9
eta = 0.8

fmin, mini, step = solve(f, g, tol, x_init, y_init,alpha, eta , xi, max_iter = 200000)
print("The solution is:", " ".join([str(x) for x in mini]))
print("Corresponding value of f(should be almost zero if solution):", fmin)
print(f"Number of steps: {step}")