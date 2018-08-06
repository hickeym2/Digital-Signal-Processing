%Lab5 Hidden Figures, Mike Hickey

%Forward Distance Equation
k = 1;
t = 0:0.001:11;
y = exp(-k*t);
plot(t,y)
axis([0 15 -2 2])

n = 0:0.001:11;
T = 2.1;
yn = (1 - k*T).^(n);
pole = -k*T + 1;

figure
subplot(3, 2, 1) %add this plot to be the first image in a 3x2 grid
plot(t,y)
axis([0 15 -2 2])
hold on

plot(t, yn)
axis([0 15 -2 2])
hold off
title("F.D T = " + T + ", Pole = " + pole)



n = 0:0.001:11;
T = 1.5;
yn = (1 - k*T).^(n);
pole = -k*T + 1;

subplot(3,2,3)
plot(t,y)
axis([0 15 -2 2])
hold on
plot(t, yn)
axis([0 15 -2 2])
hold off
title("F.D T = " + T + ", Pole = " + pole)




n = 0:0.001:11;
T = 0.8;
yn = (1 - k*T).^(n);
pole = -k*T + 1;

subplot(3,2,5)
plot(t,y)
axis([0 15 -2 2])
hold on
plot(t, yn)
axis([0 15 -2 2])
hold off
title("F.D T = " + T + ", Pole = " + pole)



%Backward Distance
n = 0:0.001:11;
T = 2.1;
yn = (1 + k*T).^(-n);
pole = 1/(k*T + 1);

subplot(3,2,2)
plot(t,y)
axis([0 15 -2 2])
hold on
plot(t, yn)
axis([0 15 -2 2])
hold off
title("B.D T = " + T + ", Pole = " + pole)




n = 0:0.001:11;
T = 1.5;
yn = (1 + k*T).^(-n);
pole = 1/(k*T + 1);

subplot(3,2,4)
plot(t,y)
axis([0 15 -2 2])
hold on
plot(t, yn)
axis([0 15 -2 2])
hold off
title("B.D T = " + T + ", Pole = " + pole)



n = 0:0.001:11;
T = 0.8;
yn = (1 + k*T).^(-n);
pole = 1/(k*T + 1);

subplot(3,2,6)
plot(t,y)
axis([0 15 -2 2])
hold on
plot(t, yn)
axis([0 15 -2 2])
hold off
title("B.D T = " + T + ", Pole = " + pole)

