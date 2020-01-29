import numpy as np

def f(x):
    return x**2 + x - 5

x = 0
y = 2
z = 12

def bisect(a, b, n):
    for i in range(n):
        d = (a + b) / 2

        if (f(d) < 0):
            a = d
        else:
            b = d
    return d
    
w = bisect(x, y, z)

print (w, f(w))


"""

def samesign(a, b):
        return a * b > 0


def bisect(func, low, high):

    assert not samesign(func(low), func(high))

    for i in range(54):
        midpoint = (low + high) / 2.0
        if samesign(func(low), func(midpoint)):
            low = midpoint
        else:
            high = midpoint

    return midpoint

def f(x):
    return x**2 + x - 5

x = bisect(f, 0, 2)
print (x, f(x))



def integration(m):
    E_m = 1 - (1/np.exp(1))

    for i in range(1, m):
      E_m = 1 - (i*E_m)

    return E_m

"""


