% Problem 4
T = 10^(-8);
n(1:1001) = 1;
yaBoi = heaviside(n)

nT = 0:T:10^-5; %10^-5 is the first 10 micro seconds
h = (10^6)*exp(-(10^6)*nT);
convolved = conv(yaBoi, h)
subplot(2,1,1)
plot(nT, convolved(1:1001))
title("Problem 4")
xlabel("Time")
ylabel("h")

% Problem 5
nT = 0:0.01:10
g = exp(-nT).*sin(nT).*cos(nT)
conv2 = conv(n, g)
subplot(2,1,2)
plot(nT, conv2(1:1001))
title("Problem 5")
xlabel("Time")
ylabel("g")