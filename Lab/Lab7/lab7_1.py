import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')

Tx = np.array(range(1, 11, 1))
t = np.linspace(-np.pi, np.pi, 1000)

i = 0
summation = 0

for T in Tx:
	n = T

	snt = ((-2)/(np.pi))*(np.cos(n*np.pi) * np.sin(n*t))/n

	summation = summation + snt

	st = t/np.pi
	
	
	plt.scatter(t, st, c="g", marker="o", label="st")
	plt.scatter(t, summation, c="r", marker="x", label="summation")
	plt.title('Problem 1, n = %s'%T)
	plt.savefig("1/lab7_1_%i.png"%i)
	plt.show()
	i+=1



