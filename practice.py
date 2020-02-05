import numpy as np 

def augment(A, b):
  Ab = np.column_stack((A, b))
  return Ab 

def first_column_zeros(A):
    B = np.copy(A)

    for i in range(len(A)):
        if (i != 0):
            B[i, :] = A[i, :] - (A[0, :]*(A[i, 0]/A[0, 0]))
    return B


def row_echelon(A, b):
    B = augment(A, b)
    for i in range(len(B)):
        B[i:, i:] = first_column_zeros(B[i:, i:])
    return B

def LU_decomposition(A):
    m, n = np.shape(A)
    U=np.copy(A)
    L=np.identity(len(A))

    for j in range(0,n):
        for i in range(j+1, m):
            L[i,j] = (U[i,j]/U[j,j])
            U[i,:] = U[i,:] - (L[i,j]*U[j,:])
    return L,U 


# Accepts a lower triangular square matrix L and a vector b, solves Ly=b for y.
def forward_substitution(L, b):
    n = len(b)
    y = [0 for i in range(len(b))]
    y[0] = b[0]/L[0][0]
    for i in range(len(b)):
        y[i] = (b[i] - np.dot(y[0], L[i][:]))/L[i][i]

    return y

A = np.array([[3, 1, -2], [1.5, 2, -5], [2, -4, 1]])
L = np.array([[1, 0, 0], [3, 1, 0], [-1.1, 2, 1]]),
b = np.array([-2.1, 1, -1])

print(forward_substitution(L,b))
