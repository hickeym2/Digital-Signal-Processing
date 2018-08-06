import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import lfilter,freqz


def signal_function(t):
	# t is a list of numbers.
	return np.cos(2*np.pi*10*t) + np.cos(2*np.pi*100*t) + np.cos(2*np.pi*200*t)
	

def fft_plots(t, v, signal_xt, abs_fft_out, ifft_out):
	###########################
	### FFT and IFTTT PLOTS ###
	###########################
	
	# Set up three subplots.
	f, xarr = plt.subplots(3)

	# Change the color of the plots.
	plt.style.use('seaborn-dark') 	#print(plt.style.available)

	# Add space between the subplots.
	plt.subplots_adjust(hspace = 1.25)
	
	# NOISY SIGNAL
	xarr[0].set_title("Noisy Signal") 	# subplot[index]
	xarr[0].set_xlabel("Time t")
	xarr[0].set_ylabel("Volts V")
	xarr[0].plot(t, signal_xt)
		
	# FFT SIGNAL	
	xarr[1].set_title("FFT Amplitude Spectrum")
	xarr[1].set_xlabel("Frequency")
	xarr[1].set_ylabel("Amplitude")
	xarr[1].plot(v[0:499], abs_fft_out[0:499])
	
	# IFFT SIGNAL
	xarr[2].set_title("Inverse FFT Amplitude Spectrum")
	xarr[2].set_xlabel("Time t")
	xarr[2].set_ylabel("Volts V")
	xarr[2].plot(t, ifft_out)
	
	return 0
	
	
def time_domain_filtering_plots(t, signal_xt, b, bn, filter_out):
	###################################
	### TIME DOMAIN FILTERING PLOTS ###
	###################################
	
	# TDFP = Time Domain Filtering Plots
	# Set up a column of subplots.
	f, tdfp = plt.subplots(3)
	
	# Change the style of the plots.
	plt.style.use("seaborn-dark")
	
	# Add space between the subplots.
	plt.subplots_adjust(hspace = 1.25)
	
	# NOISY SIGNAL
	tdfp[0].set_title("Noisy Signal") 	# subplot[index]
	tdfp[0].set_xlabel("Time t")
	tdfp[0].set_ylabel("Volts V")
	tdfp[0].plot(t, signal_xt)	
	
	# FILTER IMPULSE
	tdfp[1].set_title("Filter Impulse (YOU CAN IGNORE THIS SUBPLOT)") 	# subplot[index]
	tdfp[1].set_xlabel("Time t")
	tdfp[1].set_ylabel("Volts V")
	tdfp[1].stem(bn, b)		

	# FILTER OUTPUT (CONVOLUTION)
	tdfp[2].set_title("Filter Output (Convolution)") 	# subplot[index]
	tdfp[2].set_xlabel("Time t")
	tdfp[2].set_ylabel("Volts V")
	tdfp[2].plot(t, filter_out)			
	
	return 0

	
def frequency_domain_filtering_plots(v, abs_fft_out, hzTrue, H, w_filter_out):
	########################################
	### FREQUENCY DOMAIN FILTERING PLOTS ###
	########################################
	
	# fdf = Frequency Domain Filtering
	f, fdf = plt.subplots(3)
	
	# Change the style of the plots.
	plt.style.use("seaborn-dark")
	
	# Add space between the subplots.
	plt.subplots_adjust(hspace = 1.25)
	
	# Amplitude Spectrum (Real Half)
	fdf[0].set_title("Amplitude Spectrum (Real Half)") 	# subplot[index]
	fdf[0].set_xlabel("Frequency Hz")
	fdf[0].set_ylabel("Amplitude")
	fdf[0].plot(v[0:499], abs_fft_out[0:499])
	
	# Frequency Response of Filter
	fdf[1].set_title("Frequency Response of Filter") 	# subplot[index]
	fdf[1].set_xlabel("Frequency Hz")
	fdf[1].set_ylabel("Amplitude")
	fdf[1].plot(hzTrue[0:499], H[0:499])	
	
	# Filter Output (Fast Fourier Transform)
	fdf[2].set_title("Filter Output (fft)") 	# subplot[index]
	fdf[2].set_xlabel("Frequency Hz")
	fdf[2].set_ylabel("Amplitude")
	fdf[2].plot(v[0:499], w_filter_out[0:499])
	
	return 0
	
	
def final_plot(t, v, filter_out, filter_out_fft_out, w_filter_out, ifft_tdf):
	# fp = Final Plot
	f, fp = plt.subplots(4)
	
	# Change the style of the plots.
	plt.style.use("seaborn-dark")
	
	# Add space between the subplots.
	plt.subplots_adjust(hspace = 1.25)
	
	# FILTER OUTPUT (CONVOLUTION)
	fp[0].set_title("Filter Output (Convolution)") 	# subplot[index]
	fp[0].set_xlabel("Time t")
	fp[0].set_ylabel("Volts V")
	fp[0].plot(t, filter_out)	
	
	# FFT of Convolution
	fp[1].set_title("FFT of Time Domain Filtering (Convolution)") 	# subplot[index]
	fp[1].set_xlabel("Time t")
	fp[1].set_ylabel("Amplitude")
	fp[1].plot(v[0:499], filter_out_fft_out[0:499])
	
	# Filter Output of Frequency Domain Filtering (Fast Fourier Transform)
	fp[2].set_title("Filter Output of Frequency Domain Filter (fft)") 	# subplot[index]
	fp[2].set_xlabel("Frequency Hz")
	fp[2].set_ylabel("Amplitude")
	fp[2].plot(v[0:499], w_filter_out[0:499])
	
	# The Inverse Fast Fourier Transform of the output of the filtered waveform from FFT.
	fp[3].set_title("IFFT of FFT of Frequency Domain Filtering") 	# subplot[index]
	fp[3].set_xlabel("Time t")
	fp[3].set_ylabel("Amplitude")
	#fp[3].plot(v[0:499], ifft_tdf[0:499])
	fp[3].plot(t, ifft_tdf)	
	return 0

	
if __name__ == "__main__":
	#####################
	### FFT and IFTTT ###
	#####################

	# t is of length 1000. Numbers range from 0 to 2.
	t = np.linspace(0, 2, 1000)

	# Making a list of numbers which will make the list of frequencies.
	n = np.linspace(0, 1, 1000) # n goes from 0 to 1 with 1000 points in-between.
	
	# Create the signal xt
	signal_xt = signal_function(t)
	
	# T is the sample period
	# T = (endTime - startTime)/(signalLength)
	T = (2-0)/len(signal_xt) # T = 0.002
	
	# v is the sample frequency multiplies by the length of the function to make an array of frequencies.
	v = n/T # v ranges from 0 to 500 with 1000 samples in between.

	# Obtain the absolute value of the fast Fourier transform of the signal xt
	fft_out = fft(signal_xt)
	abs_fft_out = abs(fft_out)

	# Get the inverse Fourier transform from the fast Fourier transform.
	ifft_out = ifft(fft_out)

	
	#############################
	### TIME DOMAIN FILTERING ###
	#############################
	
	# 15 point moving average filter
	N = 15
	
	# Make list of 15 ones, and divide every single one by 15.
	b = (1/N)*np.ones(N)
	
	# Make 15 different points for graphing.
	bn = np.arange(15)
	
	# Generate a filtered output of the signal_xt, This convolves the sequence b, with the noisy data.
	filter_out = lfilter(b, 1, signal_xt)
	
	
	##################################
	### FREQUENCY DOMAIN FILTERING ###
	##################################
	
	# The rate at which the frequency is sampled.
	sample_rate = 1/T # sample_rate = 500
	
	
	# H is a representation of our moving average filter called the frequency response.
	hz, H = freqz(b, 1, worN = v*2*np.pi/sample_rate)
	hzTrue = hz*sample_rate/(2*np.pi)
	
	# Filter the fast Fourier transform of the signal xt
	w_filter_out = H*fft_out

	
	##################
	### FINAL PLOT ###
	##################
	
	# From the Time Domain Filtering.
	filter_out_fft_out = fft(filter_out) # Plot amplitude spectrum.
	
	# Take the Inverse Fast Fourier Transform of the FFT of the Time Domain Filtering.
	ifft_tdf = ifft(w_filter_out)
	
	
	#################
	### ALL PLOTS ###
 	#################
	
	# FFT and IFFT Filtering Plots 
	fft_plots(t, v, signal_xt, abs_fft_out, ifft_out)
	
	# Time Domain Filtering Plots
	time_domain_filtering_plots(t, signal_xt, b, bn, filter_out)

	# Frequency Domain Filtering Plots
	frequency_domain_filtering_plots(v, abs_fft_out, hzTrue, H, w_filter_out)
	
	# Final Plots
	final_plot(t, v, filter_out, filter_out_fft_out, w_filter_out, ifft_tdf)
	
	# Show all the plots.
	plt.show()
	