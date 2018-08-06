import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.io import wavfile

times = []

def myOwnDFT(data):
	# Start a clock timer to track how long the function takes.
	start = time.time()
	
	# The number of elements in signal u
	N = len(data)
	
	# Set up the for loop bounds
	n = np.arange(0, N)
	k = np.arange(0, N)
	sum = 0
	
	# The empty list, which will store the Fourier series.
	Un = []
	
	# Nesting for loops
	# This Outer forloop dictates what array index we are working on.
	for g in n:	
		# Reset the sum before it is appended.
		sum = 0
		
		# This forloop dictates what sum we input into the array.
		for i in k:
			# Perform Summation for value of n.
			sum = sum + data[i]*np.exp( (-2)*np.pi*1j*i*g/N )

		# Append the result of the summation to the end of Un array.
		Un = np.append(Un, sum)
		
		Un = np.absolute(Un)
		
	end = time.time()
	print("Elapsed Time: " + str(end-start) )
	
	# Store the elapsed time in an array.
	times.append(end-start)
	
	# Un is of the form np.array()
	return  Un

def makeSinWave(freq, freq_length):
	# Creating a list of frequency from 0 to freq_length in increments of 1 Hz
	t = np.linspace(0, 1, freq_length)
	
	# Create sin waves.
	return np.sin(2*np.pi*freq*t)
	
if __name__ == "__main__":
	
	end_freq = 1200
	if 1 :
		for i in range(200, end_freq, 200):
			# Make a sin wave
			sin_wave_1 = makeSinWave(10, i)
			# Get the length of the sin wave.
			length_of_sin_myDFT = np.arange(len(sin_wave_1))
			# Jam the sin wave into my DFT function.
			sin_myDFT_1 = myOwnDFT(sin_wave_1)
			
			
			# Start Plotting
			fig = plt.figure()
			fig.suptitle('myDFT of Sin Waves, size ' + str(i) , fontsize = 15)
			ax = plt.subplot(5,1,1)
			ax.set_title("Frequency 10")
			# Plot the sin wave against a list of frequencies the length of the sin wave.
			plt.plot(length_of_sin_myDFT, sin_myDFT_1)
			
			ax = plt.subplot(5,1,3)
			ax.set_title("Frequency 20")
			sin_wave_2 = makeSinWave(20, i)
			sin_myDFT_2 = myOwnDFT(sin_wave_2)
			plt.plot(length_of_sin_myDFT, sin_myDFT_2)
			
			ax = plt.subplot(5,1,5)
			ax.set_title("Frequency 30")
			sin_wave_3 = makeSinWave(30, i)
			sin_myDFT_3 = myOwnDFT(sin_wave_3)
			plt.plot(length_of_sin_myDFT, sin_myDFT_3)
			
		# Plot the times it takes to calculate all the functions
		print(times)
		print(len(times))
		fig6 = plt.figure()
		length_of_time_list = np.linspace(0, 14, len(times))
		plt.stem(length_of_time_list, times)
		plt.ylabel("Time for Completion in Seconds")
		plt.xlabel("Iteration")
	
	print("Running...")
	fig7 = plt.figure()
	# Perform the myOwnDFT on the wave file
	fs, wav_data = wavfile.read("kpt1note2k.wav")
	length_of_data = len(wav_data)
	wav_myOwnDFT = myOwnDFT(wav_data)
	plt.plot(np.arange(length_of_data), wav_myOwnDFT)
	plt.suptitle("kpt1note2k.wav through myOwnDFT")
	plt.xlabel("Frequency in Hz")
	plt.ylabel("Amplitude")
	plt.show()

