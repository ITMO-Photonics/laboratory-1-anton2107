import scipy.optimize as opt
import math as m
import timeit
a = .1
b = 2.4
def f(x):
    return m.cos(x)/(1+x**2)
print('x =', opt.bisect(f,a,b,xtol=1e-15), 'by bisection method')
print("The executing time is", timeit.timeit('opt.bisect(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b', number=1000)/1000)
print('x =', opt.newton(f,b/2-a/2,tol=1e-15), 'by Newton method')
print("The executing time is", timeit.timeit('opt.newton(f,b/2-a/2,tol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=1000)/1000)
print('x =', opt.ridder(f,a,b,xtol=1e-15), 'by Ridder method')
print("The executing time is", timeit.timeit('opt.ridder(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=1000)/1000)
print('x =', opt.brentq(f,a,b,xtol=1e-15), 'by Brent quadratic method')
print("The executing time is", timeit.timeit('opt.brentq(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=1000)/1000)
print('x =', opt.brenth(f,a,b,xtol=1e-15), 'by Brent hyperbolic method')
print("The executing time is", timeit.timeit('opt.brenth(f,a,b,xtol=1e-15)', setup='from __main__ import opt, m, f, a, b',  number=1000)/1000)
