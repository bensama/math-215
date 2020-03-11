import numpy as np

def subscriber_vals(x_0,k):
	P = np.array([[0.7, 0.2],[0.3, 0.8]])
	for i in range(k):
		x_0 = P@x_0
	return x_0


z_0 = np.array([0.6, 0.4])

netflix_subs6 = subscriber_vals(z_0,6)