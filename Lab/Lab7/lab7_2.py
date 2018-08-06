import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')

Tx = np.array(range(1, 20, 1))
t = np.linspace(-np.pi, np.pi, 1000)

i = 0
summation = 0

for T in Tx:
	n = T
	L = 5
	scalar = 4/(np.pi * n)
	snt = scalar * ( np.sin(n*np.pi*t/L) )
	
	# If you do not save the figure before you show it, the .png will be corrupted.	
	# Is i an even number?
	if(T % 2 == 1):
		summation = summation + snt

		st = t/np.pi
		
		plt.scatter(t, st, c="g", marker="o", label="st")
		plt.scatter(t, summation, c="r", marker="x", label="summation")
		

		plt.title('Problem 2, n = %s'%T)
		plt.savefig('2/lab7_2_%i.png'%i)
		i+=1

		plt.show()

