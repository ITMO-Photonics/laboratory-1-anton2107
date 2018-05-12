import scipy.linalg as sl
import numpy as np
import timeit
N=10
B=np.zeros((N))
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
k=1
t=tstart
while k<=1000:
    while t<=tfinish:
        sl.solve(A,b(t))
        t=t+deltat
    k+=1
print('The efficiency of the scipy.linalg.solve method can be estimated by the solving time which is', (timeit.default_timer()-a)/1000, 's')

a = timeit.default_timer()
k=1
t=tstart
lu,piv=sl.lu_factor(A,overwrite_a=False)
while k<=1000:
    while t<=tfinish:
        sl.lu_solve((lu,piv),b(t),trans=0)
        t=t+deltat
    k+=1
print('The efficiency of the scipy.linalg.lu_solve method can be estimated by the solving time which is', (timeit.default_timer()-a)/1000, 's')

a = timeit.default_timer()
k=1
t=tstart
while k<=1000:
    while t<=tfinish:
        np.dot(sl.inv(A),b(t))
        t=t+deltat
    k+=1
print('The efficiency of the scipy.linalg.inv method can be estimated by the solving time which is', (timeit.default_timer()-a)/1000, 's')
