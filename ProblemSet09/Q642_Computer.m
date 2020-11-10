% Landon Buell
% Q 6.4.2 - Computer Probs
% MATH 753.01
% 10 Nov 2020

t0 = 0;
tf = 1;
h = 0.1;
y0 = 1;
t = [t0:h:tf];

format long;

%%%% Solve Part A %%%%
disp("Part A");
ODE_A = @(t,y) t;
Sol_A = @(t) 0.5 * t.^2 + 1;
yA = Sol_A(t);
wA = RungeKutta4(ODE_A,t,y0);
err_A = yA - wA; 
TableA = [t' , yA' , wA' , err_A']

%%%% Solve Part C %%%%
disp("Part C");
ODE_C = @(t,y) 2*(t+1)*y;
Sol_C = @(t) exp(t.^2 + 2*t );
yC = Sol_C(t);
wC = RungeKutta4(ODE_C,t,y0);
err_C = yC - wC; 
TableC = [t' , yC' , wC' , err_C']

%%%% Solve Part E %%%%
disp("Part E");
ODE_E = @(t,y) 1/y^2;
Sol_E = @(t) (3*t+1).^(1/3);
yE = Sol_E(t);
wE = RungeKutta4(ODE_E,t,y0);
err_E = yE - wE; 
TableE = [t' , yE' , wE' , err_E']