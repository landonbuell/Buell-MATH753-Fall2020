% Landon Buell
% MATH 753.01 - Fall 2020
% HW 09 - Q 6.4.3
% 2 November 2020

t0 = 0;
tf = 1;
h = 1/4;
y0 = 1;
t = [t0:h:tf];

%%%% Solve Part A %%%%
disp("Part A");
ODE_A = @(t,y) t;
Sol_A = @(t) 0.5 * t.^2 + 1;
yA = Sol_A(t);
wA = RungeKutta4(ODE_A,t,y0);
err_A = yA - wA; 

%%%% Solve Part C %%%%
disp("Part C");
ODE_C = @(t,y) 2*(t+1)*y;
Sol_C = @(t) exp(t.^2 + 2*t );
yC = Sol_C(t);
wC = RungeKutta4(ODE_C,t,y0);
err_C = yC - wC; 

%%%% Solve Part E %%%%
disp("Part E");
ODE_E = @(t,y) 1/y^2;
Sol_E = @(t) (3*t+1).^(1/3);
yE = Sol_E(t);
wE = RungeKutta4(ODE_E,t,y0);
err_E = yE - wE; 