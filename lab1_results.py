
# coding: utf-8

# In[1]:


import math
R = 8
L = 4
V = math.pi * R **2 * L
print(V)


# In[2]:


import scipy.optimize as opt
import math as m
import timeit
a = .1
b = 2.4
def f(x):
    return m.cos(x)/(1+x**2)
print('x =', opt.bisect(f,a,b,xtol=1e-15), 'by bisection method')
get_ipython().run_line_magic('timeit', 'opt.bisect(f,a,b,xtol=1e-15)')
print('x =', opt.newton(f,b/2-a/2,tol=1e-15), 'by Newton method')
get_ipython().run_line_magic('timeit', 'opt.ridder(f,a,b,xtol=1e-15)')
print('x =', opt.ridder(f,a,b,xtol=1e-15), 'by Ridder method')
get_ipython().run_line_magic('timeit', 'opt.brentq(f,a,b,xtol=1e-15)')
print('x =', opt.brentq(f,a,b,xtol=1e-15), 'by Brent quadratic method')
get_ipython().run_line_magic('timeit', 'opt.brentq(f,a,b,xtol=1e-15)')
print('x =', opt.brenth(f,a,b,xtol=1e-15), 'by Brent hyperbolic method')
get_ipython().run_line_magic('timeit', 'opt.brenth(f,a,b,xtol=1e-15)')


# In[16]:


import scipy.linalg as sl
import numpy as np
N=10
A=np.zeros((N,N))
B=np.zeros((N))
i,j=np.indices(A.shape)
for k in range(int(N)):
    A[i==j+k]=1
    B[k]=k
print('A - matrix:')
print(A)
print('B - vector:')
print(B)
print('Answer vector:')
print(sl.solve(A,B))


# In[41]:


import scipy.linalg as sl
import numpy as np
N=10
tstart=0.
tfinish=10.
deltat=0.1
A=np.random.random((N,N))
def b(time):
    for k in range(int(N)):
        B[k]=k/(1+k*time)
    return B
t=tstart
while t<=tfinish:
    print('t =', t, 'and x(t) =')
    print(sl.solve(A,b(t)))
    t=t+deltat
cstart=sl.solve(A,b(tstart))
cfinish=sl.solve(A,b(tfinish))
print('The total x(t) change is', cfinish - cstart)

a = timeit.default_timer()
t=tstart
while t<=tfinish:
    sl.solve(A,b(t))
    t=t+deltat
print('The efficiency of the scipy.linalg.solve method is', timeit.default_timer()-a, 's')

