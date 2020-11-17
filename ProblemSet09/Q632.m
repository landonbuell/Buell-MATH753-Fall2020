% Landon Buell
% Q 6.2.2 - Computer Probs
% MATH 753.01
% 10 Nov 2020


t = (0:0.25:1);
ODE = @(y) [y(1) + y(2) ; -y(1) + y(2)];
y0 = [1,0];

TrapezoidMethofMultiD(ODE,t,y0);
