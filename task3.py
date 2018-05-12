import scipy.linalg as sl
import numpy as np
N=20
A=np.zeros((N,N))
B=np.zeros((N))
i,j=np.indices(A.shape)
for k in range(3):
    A[i==j+k]=1
    B[k]=k
print('A - matrix:')
print(A)
print('B - vector:')
print(B)
print('Answer vector:')
print(sl.solve(A,B))
