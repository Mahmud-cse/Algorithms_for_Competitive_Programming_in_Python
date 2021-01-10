"""
how to calculate binomial coefficient, assuming their answer is 
less than 32 bits?
Calculate their value modulo the 8th Mersenne prime (2147483647)
"""

from collections import *
import sys  

input=sys.stdin.readline

#################################################
##template to calculate binomial coef %MOD from nehan_der_thal


MOD = 2147483647 #big prime 
#MOD = 10**9+7 #another big prime

 
def mul(a, b):
    return ((a % MOD) * (b % MOD)) % MOD
 
def div(a, b):
    return mul(a, pow(b, MOD-2, MOD))
 
def div2(a, b):
    return mul(a, modinv(b))
 
def modinv(a):
    b, u, v = MOD, 1, 0
    while b:
        t = a//b
        a, u = a-t*b, u-t*v
        a, b, u, v = b, a, v, u
    u %= MOD
    return u
 
def frac(limit):
    frac = [1]*limit
    for i in range(2,limit):
            frac[i] = i * frac[i-1]%MOD
    fraci = [None]*limit
    fraci[-1] = pow(frac[-1], MOD -2, MOD)
    for i in range(-2, -limit-1, -1):
            fraci[i] = fraci[i+1] * (limit + i + 1) % MOD
    return frac, fraci
 
frac, fraci = frac(1341398)
#calculate C(n,k) n = a, k = b 
def cmb(a, b):
    if not a >= b >= 0:
            return 0
    return frac[a]*fraci[b]*fraci[a-b]%MOD

#################################################
    
def ri():
    return int(input())
 
def rl():
    return list(map(int, input().split()))

#print Pascal triangle to check that this program works
#even thought this program doesnt rely on Pascal triangle at all for calculcations
#this program can just calculate any binomial coef out of the blue, modulo a big prime
for n in range(1, 10):
    for k in range(n+1):
        print(cmb(n,k), end =" ")
    print()

