"""
Successive parabolic interpolations:

    We iteratively chose 3 points, draw a parabola y = Ax^2 + Bx + C 
    find the minimum point of that parabola (-B/2A)
    Then now we have 4 points (3 initial point and that minimum), 
    we keep the 3 points with the smalest values out of the 4
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

def parabolic_interpolations(f, a, b, tol):
    """
    We iteratively chose 3 points, draw a parabola y = Ax^2 + Bx + C 
    find the minimum point of that parabola (-B/2A)
    Then now we have 4 points (3 initial point and that minimum), 
    we keep the 3 points with the smalest values out of the 4
    for next iteration
    """
    c = (a + b) / 2
    fa, fb, fc = f(a), f(b), f(c)

    while abs(fb - fa) > tol:
        x = [a,b,c]
        y  = [fa, fb, fc]
        A,B,C = parabola_coefficients(x,y)
        mini = - B / (2*A)
        fmini = f(mini)
        points = [(fa, a), (fb, b), (fc, c), (fmini, mini)]
        points.sort()
        fa, a = points[0]
        fc, c = points[1]
        fb, b = points[2]

    return a

#example use

#testcase 1
from math import sin
a = 2.
b = 7.
tol = 0.000001
f = sin
result = parabolic_interpolations(f, a, b, tol)
print(result) #4.712388985743289

#testcase 2
f = lambda x: x**1.8 - 15*x + 4
a = 2.
b = 30.
tol = 0.000001
result = parabolic_interpolations(f, a, b, tol)
print(result) # 14.158702029267767

