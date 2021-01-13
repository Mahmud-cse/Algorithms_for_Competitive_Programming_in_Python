"""
we iteratively chose 3 points, draw a parabola, find the minimum of that parabola
then now we have 4 points, we take the 3 with the smalest values and iterate
"""


def parabola_coefficients(x,y):
    x_1 = x[0]
    x_2 = x[1]
    x_3 = x[2]
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]

    A = y_1/((x_1-x_2)*(x_1-x_3)) + y_2/((x_2-x_1)*(x_2-x_3)) + y_3/((x_3-x_1)*(x_3-x_2))

    B = (-y_1*(x_2+x_3)/((x_1-x_2)*(x_1-x_3))
         -y_2*(x_1+x_3)/((x_2-x_1)*(x_2-x_3))
         -y_3*(x_1+x_2)/((x_3-x_1)*(x_3-x_2)))

    C = (y_1*x_2*x_3/((x_1-x_2)*(x_1-x_3))
        +y_2*x_1*x_3/((x_2-x_1)*(x_2-x_3))
        +y_3*x_1*x_2/((x_3-x_1)*(x_3-x_2)))

    return A, B, C

def parabolic_interpolations(f, a, b, tol):
    c = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fc = f(c)
    while abs(fc - fa) > tol:
        x = [a,b,c]
        y  = [fa, fb, fc]
        A,B,C = parabola_coefficients(x,y)
        mini = - B / (2*A)
        fmini = f(mini)
        points = [(fa, a), (fb, b), (fc, c), (fmini, mini)]
        points.sort()
        fa, a = points[0]
        fb, b = points[1]
        fc, c = points[2]

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

