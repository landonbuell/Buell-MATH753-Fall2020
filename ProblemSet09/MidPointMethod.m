function [vals] = MidpointMethod(func,t,y0)
%MidPointMethod Solve 1st order ODE with Euler's Method
% func : right side of eqn
% t : time axis
% y0 : starting function value
% step : step size 

step = t(2) - t(1);
w = zeros(size(t));
w(1) = y0;

for i = 1:length(t)-1
    f1 = func(t(i),w(i));
    t_step = t(i) + step/2;
    w_step = w(i) + (step/2) * f(t(i),w(i)); 
    w(i+1) =  w(i) + step*func(t_step,w_step);
end

vals = w;
end

