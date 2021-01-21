"""
Armijo rule

we fix a constant C1 < 1 (which should depend on the curvature of the function)
We want C1 as small as possible, but we have to 
adapt it to the curvature.

And we want to find a big alpha to do gradient descent
but we want small enough so that it still verifies
a condition similar to Taylor developement
NOTE :
################################################################## 
at this point we could do a line search to find the best alpha
when we minimize in the direction of the gradient
OR  
we use Armijo to find a rather small alpha 
(so that a condition similar to Taylor is true
and we can use it to make a step in a direction 
that minimize f)
The algo help us to have an alpha small,
....but not too small either.
##################################################################
More details on Armijo rule:

we know for alpha super small, we can verify that inequality:
f(x - alpha * gradf) less than f(x) - C * alpha * ||gradf(x)||**2   (*)
(it comes from some conditions on the curvature of f in the neighborood of x)

algorithm is like this:
we start from a value beta..... ie alpha = beta  
beta is small, less than 1

1/ if the inequality (*) is already verified by this alpha
bingo!!!
we try to increase alpha :  # alpha /= beta  
(it increases because beta is small)
until (*) is not true anymore, then we stop

2/ if the inequality is not verified initially
we keep reducing alpha until we find one that works 
(we reduce alpha by doing alpha *= beta with beta < 1)

Another way to understand that algo is that we try a lot of powers of beta
{ ....beta^k, ....beta^2, beta, 1, 1/beta, (1/beta)^2, ....(1/beta)^k, ...}
we start somewhere, for example at beta, and by successive itreations,
we try to find the biggest alpha in those iteration that verifies (*)

Once again there is no guarantee at all that this alpha
is the biggest that verifies (*)
the algo is just a convenient (and reasonably fast) way to find an alpha
that works.

"""


def df(x, epsilon):
	return (f(x + epsilon) - f(x - epsilon))/ (2 * epsilon)

def g(alpha, C, x, dfx):
	return f(x) - C * alpha * (dfx**2) - f(x - alpha * dfx)

def armijo(f, a, b, tol, C1, C2, max_iter = 1000):
	beta = 1 / C2
	x = (a + b) / 2
	x_new = b
	step = 0
	while abs(x - x_new) > tol and step < max_iter:
		step += 1
		alpha = beta
		
		max_iter_armijo = 100
		curr_iter_armijo = 0
		while g(alpha, C1, x, df(x, tol)) < 0:
			curr_iter_armijo += 1
			if curr_iter_armijo > max_iter_armijo:
				return x_new, step
			alpha *= beta
			

		while g(alpha / beta, C1, x, df(x, tol)) > 0:
			alpha = alpha / beta

		x_new = x - alpha * df(x, tol)
		if x_new >= b:
			x_new = b
		elif x_new < a:
			x_new = a

		x, x_new = x_new, x
		

	return x_new, step

#testcase 1:
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin

mini, step  = armijo(f, a, b, tol, 0.8, 3)
print(f"Minimum of f is: {mini}, and we needed {step} steps.")

#testcase 2:
from math import sin
f = lambda x: x**1.8 - 15*x + 4 - sin(x)
a = 2.
b = 30.
tol = 0.000001

mini, step  = armijo(f, a, b, tol, 0.8, 3)
print(f"Minimum of f is: {mini}, and we needed {step} steps.")

