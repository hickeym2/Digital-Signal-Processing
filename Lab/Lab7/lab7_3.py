import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')

Tx = np.array(range(1, 20, 1))
t = np.linspace(-np.pi, np.pi, 1000)

i = 1
summation = 0

for T in Tx:
	n = T

	if T % 2 != 0:
		L = np.pi

		scalar = (8)/((np.pi)**2)
		exponent = (n-1)/2
		num = (-1)**exponent
	
		den = (n**2)
		snt = scalar * num * ( np.sin(n*np.pi*t/L) )/den
	
		summation = summation + snt
	
		st = t/np.pi
		
		plt.scatter(t, st, c="g", marker="o", label="st")
		plt.scatter(t, summation, c="r", marker="x", label="summation")
	
		if n != 0 or n != 1:
			plt.title('Problem 3, n = %s'%T)
			plt.savefig('3/lab7_2_%i.png'%i)
			i+=1
			plt.show()

