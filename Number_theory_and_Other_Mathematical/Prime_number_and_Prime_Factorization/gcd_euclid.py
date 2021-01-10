def gcd(a, b):  
    if a < b:
        return gcd(b, a)
    while b != 0:
        a, b  = b, a % b
    return a