import numpy as np

def integration(m):
    E_m = 1 - (1/np.exp(1))

    for i in range(m - 1):
        E_m = 1 - i*E_m

    return E_m



