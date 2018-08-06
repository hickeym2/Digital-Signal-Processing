import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile

def analyzeWave(wave):
	# Read in the input audio file.
	# fs = Frequency Sample in samples per second. 
	# data = The data from the wave.
	fs, data = wavfile.read(wave)
	
	# Find the total time of the wave file.
	# t = nT
	total_time = len(data)/fs
	
	print(total_time)
	
	# Take the Fast Fourier Transform of the data.
	fftOut = fft(data)
	
	# Make a list of sample indices.
	n = np.arange(len(data))
	
	# T = the duration of time between samples.
	T = 1/total_time
	
	# Multiplying the sample frequency by every data sample.
	freqLabel = T * n
	
	# Plot the data.
	plt.plot(freqLabel, abs(fftOut))
	
	# Format the title and axis.
	title = 'Piano Note Analysis ' + wave
	plt.title(title)
	plt.xlabel('Frequency (Hz)')
	plt.ylabel('Amlpitude')
	
	# Highest note on a piano
	highest_note = 4186.01
	# highest_note = 750
	min = 0
	# min = 200
	max = highest_note
	
	# Set the limits of the x axis to be from 0 to the highest possible piano note in Hz.
	plt.xlim((min, max))
	
	# Show the plot.
	plt.show()
	
if __name__ == "__main__":
	analyzeWave('hkp.wav')
	analyzeWave('kpt.wav')