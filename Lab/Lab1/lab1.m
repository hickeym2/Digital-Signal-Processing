%Problem1

% d = 5
% x = 0:0.01:10
% graph = heaviside(x-d)
% plot(x, graph)
% xlabel("Time")
% ylabel("Amplitude")
% title("Unit Step Function")
% ylim([-2 2])

%Problem2, if the sampling rate of x is changed
%to a larger number, the function appears differently
%x = 0:1:10 will have a piece wise attribute with a slope of 1

%Problem3
% T = 0.1 %amount of time between each sample
% k = 0:99 %iterator, the k-th sample
% A = 1
% alpha = 0.8
% n = k*T
% y = A*alpha.^n
% x = n
% 
% stem(x,y)
% xlabel("k*T")
% ylabel("A*alpha.^n")
% title("Problem3 alpha = 0.8")

%Problem4
% T = 0.1 %amount of time between each sample
% k = 0:99 %iterator, the k-th sample
% A = 1
% alpha = 1.6
% n = k*T
% y = A*alpha.^n
% x = n
% 
% stem(x,y)
% xlabel("k*T")
% ylabel("A*alpha.^n")
% title("Problem4 alpha = 1.6")

%Problem5
% T = 0.1 %amount of time between each sample
% k = 0:49 %iterator, the k-th sample
% A = 1
% alpha = 1
% n = k*T
% y = A*alpha.^n
% x = n
% ylim([-1 2])
% stem(x,y)
% xlabel("k*T")
% ylabel("A*alpha.^n")
% title("Problem5")


%Problem6
% k = 0:24
% T = 1
% n = k*T
% XofN = cos((pi*n)/4)
% subplot(2,1,1)
% plot(n, XofN)
% xlabel("k*T")
% ylabel("XofN = cos((pi*n)/4)")
% title("Problem6")

%Problem 7
% k = 0:24
% T = 1
% n = k*T
% subplot(2,1,2)
% X1ofN = cos((pi*(n+8))/4)
% plot(n, X1ofN)
% xlabel("k*T")
% ylabel("cos((pi*(n+8))/4)")
% title("Problem7")
% %Same thing.
% 
% 
% %Problem8
% k = 0:24
% T = 1
% X2ofN = cos((3*pi*k*T)/8)
% subplot(2,1,1)
% plot(k*T, X2ofN)
% xlabel("k*T")
% ylabel("cos((3*pi*k*T)/8)")
% title("Problem8.1")
% 
% X3ofN = cos((3*pi*(k*T+16))/8)
% subplot(2,1,2)
% plot(k*T, X3ofN)
% xlabel("k*T")
% ylabel("cos((3*pi*(k*T+16))/8)")
% title("Problem8.2")
% Same Thing

% Problem9
% The sinusoid from problem 7 has a higher frequency
% Than the sinusoid from problem 8 because the definition
% of wavelength is the distance between two corresponding points.
% Since problem7's sinusoid takes less time to complete one wavelength,
% this sinusoid has a higher frequency.

% Problem 10
% The sinusoid from problem8 takes more time to achieve periodic behabior.
