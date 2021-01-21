#number of steps: only 7 steps, so it is much less than golden ratio
#however each step takes more time because we need to compute 
#the parabola coeficient

"""
Successive parabolic interpolations:

    We iteratively chose 3 points, draw a parabola y = Ax^2 + Bx + C 
    find the minimum point of that parabola (-B/2A)
    Then now we have 4 points (3 initial point and that minimum), 
    we take the 3 with the smalest values out of 4
    for next iteration

Side notes:
Note that the parabola we chose depends on our coordinate system
for 3 given points in the plane, we could find another parabola
x = Dy^2 + Ey + F
or we could find many other parabola with different angles

Also note that we did find the parameters A,B and C
of the parabola using Lagrange polynomial:
https://en.wikipedia.org/wiki/Lagrange_polynomial
"""

def parabola_coefficients(x,y):
    """
    returns the coeficients (A,B,C)of the parabola Ax^2 + Bx + C
    that contains the 3 poins of coordinate x, y
    input: x is a 3-tuple containing x-axis coordinates
    and y is a 3-tuple containing y-axis coordinates
    """
    x_1, x_2, x_3 = x
    y_1, y_2, y_3 = y

    A = y_1/((x_1-x_2)*(x_1-x_3))   \
        + y_2/((x_2-x_1)*(x_2-x_3)) \
        + y_3/((x_3-x_1)*(x_3-x_2))

    B = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
         -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
         -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

    C = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
        +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
        +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

    return A, B, C

def parabolic(f, a, b, tol, max_iter = 1000):
    m = (a + b) / 2
    fa, fm, fb = f(a), f(m), f(b)
    step = 0

    while abs(b - a) > tol and step < max_iter:
        step += 1

        #computation of minimum of local parabola
        x = a, m, b
        y = fa, fm, fb
        A, B, C = parabola_coefficients(x,y)
        p = -B / (2*A)
        fp = f(p)

        #early termination if f(p) is not usefull
        # if fp > max(fa,fm,fb):
        #     return m, step

        #we get rid of the biggest f value
        points = [(fa, a), (fm, m), (fp, p), (fb, b)]
        points.sort()
        points.pop()

        #prepare values for next iteration
        points.sort(key=lambda x: x[1])
        (fa, a), (fm, m), (fb, b) = points

    return m, step


#example use

#testcase 1
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
mini, step = parabolic(f, a, b, tol, max_iter = 1000)
print(mini) #4.712388985743289
print(f"The number of steps needed is {step}.") #7

#testcase 2
f = lambda x: x**1.8 - 15*x + 4
a = 2.
b = 30.
tol = 0.000001

mini, step = parabolic(f, a, b, tol, max_iter = 1000)
print(mini)#14.158697839930518
print(f"The number of steps needed is {step}.") #7
print(f(mini))
print(f(14.158702029267767)) # we get better result than what was asked