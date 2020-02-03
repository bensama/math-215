import numpy as np 


def first_column_zeros(A):
    B=np.copy(A)
    
    for i in range(1, 3):
        B[i,:] = A[i,:]-(A[i,0]/A[0,0])
    return B

X = np.array([[1,1,1],[1,4,2],[4,7,8]])
y = np.array([1,3,9])
A=np.array([[2,1,3,1],[1,2,-1,2.5],[4,2,-1,1]])

print(first_column_zeros(A))
