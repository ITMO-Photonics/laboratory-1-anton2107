import scipy.optimize as opt
import math as m
import timeit
a = .1
b = 2.4
def f(x):
    return m.cos(x)/(1+x**2)
print('x =', opt.bisect(f,a,b,xtol=1e-15), 'by bisection method')
%timeit opt.bisect(f,a,b,xtol=1e-15)
print('x =', opt.newton(f,b/2-a/2,tol=1e-15), 'by Newton method')
%timeit opt.ridder(f,a,b,xtol=1e-15)
print('x =', opt.ridder(f,a,b,xtol=1e-15), 'by Ridder method')
%timeit opt.brentq(f,a,b,xtol=1e-15)
print('x =', opt.brentq(f,a,b,xtol=1e-15), 'by Brent quadratic method')
%timeit opt.brentq(f,a,b,xtol=1e-15)
print('x =', opt.brenth(f,a,b,xtol=1e-15), 'by Brent hyperbolic method')
%timeit opt.brenth(f,a,b,xtol=1e-15)
