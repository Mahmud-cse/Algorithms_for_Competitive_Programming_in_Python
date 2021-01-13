
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
    while abs(fb - fa) > tol:
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

result = parabolic_interpolations(f, a, b, tol)
print(result)

