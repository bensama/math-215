import numpy as np
import matplotlib.pyplot as plt

X3 = np.array([[1, np.log(87.77)], [1, np.log(224.70)], [1, np.log(365.25)], [1, np.log(686.95)], [1, np.log(4332.62)], [1, np.log(10759.2)]])

Y3 = np.array([np.log(0.389), np.log(0.724), np.log(1), np.log(1.524), np.log(5.2), np.log(9.510)])

# Replace the values of 0 with the normal equation coefficient matrix and normal equation right-hand side from Problem 7.

normal_coef3 = np.array(np.matmul(np.transpose(X3), X3))

normal_vect3 = np.array(np.matmul(np.transpose(X3), Y3))

# Replace the value of 0 with the least squares solution from Problem 7.

beta3 = np.linalg.solve(normal_coef3, normal_vect3)

"""**Problem 8**"""

# Replace the values of 0 with your predictions for the semi-major axes of Uranus and Neptune.


# pred_Uran = (beta3[0] + (beta3[1]*30687.15))
pred_Uran = (((beta3[0])*(30687.15))**beta3[1])

pred_Nept = (beta3[0] + (beta3[1]*60190.03))

# print(beta3)
print(pred_Uran)
print(pred_Nept)
