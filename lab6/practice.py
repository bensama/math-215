import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([[1, 5], [1, 10], [1, 15], [1, 20], [1, 25], [1, 30], [1, 35], [1, 40], [1, 45], [1, 50]])
Y1 = np.array([[3.33], [4.43], [4.39], [5.23], [5.67], [6.06], [7.01], [7.16], [8.03], [8.78]])

# print(np.matmul(np.transpose(X1), Y1))

normal_coef1 = np.array([[10, 275], [275, 9625]])

normal_vect1 = np.array([[60.09], [1887.05]])

beta1 = np.array([[2.88133333], [0.11373333]])

def ls1_line(x):
    y = beta1[0] + (beta1[1]*x)
    return y

def create_plots1():
  time = np.array([[5], [10], [15], [20], [25], [30], [35], [40], [45], [50]])
  vel = np.array([[3.33], [4.43], [4.39], [5.23], [5.67], [6.06], [7.01], [7.16], [8.03], [8.78]])

  plt.plot(vel, time)
  plt.show()
  return None

pred1 = 0

X2 = np.array([[5, 5**2], [10, 10**2], [15, 15**2], [20, 20**2], [25, 25**2],[30, 30**2], [35, 35**2], [40, 40**2], [45, 45**2], [50, 50**2]])

Y2 = np.array([[20.57], [87.48], [197.45], [347.67], [546.12], [784.35], [1066.02], [1390.97], [1761.85], [2177.34]])

# print(np.matmul(np.transpose(X2), X2))
# print(np.matmul(np.transpose(X2), Y2))

normal_coef2 = np.array([[9625, 378125], [378125, 15833125]])

normal_vect2 = np.array([[329176.05], [13782519.25]])

beta2 = np.array(np.linalg.solve(normal_coef2, normal_vect2))

def ls2_par(x):
  y = (beta2[0]*x) + (beta2[1]*(x**2))
  return y

print(ls2_par(60))