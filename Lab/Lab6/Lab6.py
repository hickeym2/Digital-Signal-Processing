import numpy as np # Importing the library numpy into the script and reducing its library to a nickname called np
import scipy.signal as sig # Import the signals sub-library of the whole scipy library. Nickname it to sig.
import matplotlib.pyplot as plt # Import the matplotlib sub-library pyplot, which will be used for plotting, nickname it as plt.

# print(plot.style.available) # Will print out all the available parameters for plot.style.use(<'style'>)
plt.style.use('seaborn-dark') # Change the background of the plot and the line color of the plot. I chose seaborn-dark.


Tx = np.linspace(0, 0.22, 5) # Making a variable called Tx. Using the numpy library with np. calling the function linspace()
# linspace will return evenly spaced numbers over a specific interval.
# linspace(start number, end number, how many numbers to space the sequence by)
# np.linspace(o, 0.22, 5) # I want 5 numbers evenly spaced out between the values 0 to 0.22

i = 0 # i is a counter.

for T in Tx:	# Making a for loop. Iterator is T. and we are going to loop through Tx. (5 numbers between 0 and 0.22)
	#Notice the indent to designate the forloops code block
	num = np.array([10-10*np.exp(-T)]) # Calling the numpy library. Asking for the function Array. We want to make an array.
	# So we are building an array which will be 5 numbers because we are using T to loop through Tx
	# num stands for numerator

	den = np.array([1, 10-11*np.exp(-T)]) # making a tuple

	dtf = sig.dlti(num, den) # some discrete time linear time invariant system base class. Like a multi dimensional array.

	t,y = sig.dstep((dtf), n = 1000) # dstep returns a tuple. Returns two things. We store the discription of dtf in a tuple.
	# So it is a 1D array, and the step response of the system

	tCirc = np.linspace(0, 2*np.pi, 100) # making 100 evenly spaced number between 0 to 2*3.14

	xCirc = np.cos(tCirc) # Using Numpy, asking for the cosign function, giving it the 100 numbers we just made.

	yCirc = np.sin(tCirc) # Same thing as xCirc but for the y direction.

	poleLocation = np.roots(den) # Finding what makes the denominator zero.

	colorIndicator = "b" # Assigning a char to this variable. b for blue

	markerIndicator = "o" # Using o the litteral symbol that will be plotted on the graph.
	# We will plot a blue "o" for a stable poll

	
	# Notice that this if statement is more indented while still being in the for loop.
	# Making an if statement to see if the absolute value of the pole location is greater than 1.
	# This is checking the stability of the system
	if (np.abs(poleLocation)>1):
		# If the pole is unstable 
		colorIndicator = "r" # red
		markerIndicator = "x" # plotting a red x for an unstable poll
		
	# Ending the if statement
	

	print('Pole Location = ', poleLocation) # Display the value of the variable poleLocation on the screen.

	# using the matplotlib library as plt and calling the subplots function.
	# Subplots returns multiple things which we will store in f and xarr
	# subplots is being given the number of rows.
	f, xarr = plt.subplots(2) # we have two subploy positions. Row 1 and Row 2, Indexed as 0 and 1
	
	# xarr[<subplot index>]
	xarr[0].set_title('T = %s'%T) # Setting the title to a string. Calling the iterator T as a string.

	xarr[0].plot(t, y[:][0]) # Plotting y against t, where y is an array of dynamic size.
	# We dont know the size of y, so we want to use all of it, starting at index 0
	# Remember that t is a 1-Dimensional array. A sequence.

	#New plot position index 1 (the second plot)
	xarr[1].plot(1, 0, c = "g", marker = "o") # the color green with symbol 'o' is going to be placed at 1,0
	
	
	# plot the circle components
	xarr[1].plot(xCirc, yCirc)

	# for the pole locations we are going to either plot a blue "o" or a red "x" depending if the pole is stable or not.
	xarr[1].scatter(poleLocation, 0, c=colorIndicator, marker=markerIndicator) # poleLocation is x, and we dont want to rise in the y

	xarr[1].set_xlabel("Pole Magnitude = %s"%poleLocation) # Making the x label say the pole's magnitude

	xarr[1].set_xlim([-2,2]) # making the graph have some extra white space on the x axis.

	plt.savefig('animations%i.png'%i) # We dont want to overwrite the files. So we increment i and make multiple saves

	plt.show() # final plot

	i+=1 # Increment the current value of i, we don't want to overwrite the files.
	





