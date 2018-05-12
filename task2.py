import scipy.optimize as opt
import math as m
import timeit
from sympy import diff, symbols, cos

a = .1
b = 2.4
x = symbols('x')

def f(x):
    return m.cos(x)/(1+x**2)

print("The f(x) function is cos(x)/(1+x**2)")
print("The f(x) derivative is", diff(cos(x)/(1+x**2)))

def df(x):
    return -2*x*m.cos(x)/(x**2+1)**2-m.sin(x)/(x**2+1)

print('x =', opt.bisect(f,a,b,xtol=1e-15), 'by bisection method')
print("The executing time is", timeit.timeit('opt.bisect(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b', number=10000)/10000)

print('x =', opt.newton(f,b/2-a/2,tol=1e-15), 'by secant method')
print("The executing time is", timeit.timeit('opt.newton(f,b/2-a/2,tol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=10000)/10000)

print('x =', opt.newton(f,b/2-a/2,fprime=df,tol=1e-15), 'by Newton method')
print("The executing time is", timeit.timeit('opt.newton(f,b/2-a/2,fprime=df,tol=1e-15)', setup='from __main__ import opt, m, f, df, a, b',  number=10000)/10000)

print('x =', opt.brentq(f,a,b,xtol=1e-15), 'by Brent quadratic method')
print("The executing time is", timeit.timeit('opt.brentq(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=10000)/10000)
