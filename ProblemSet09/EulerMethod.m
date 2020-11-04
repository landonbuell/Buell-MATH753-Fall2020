function [vals] = EulerMethod(func,t,y0)
%EulerMethod Solve 1st order ODE with Euler's Method
% func : right side of eqn
% t : time axis
% y0 : starting function value
% step : step size 

step = t(2) - t(1);
w = zeros(size(t));
w(1) = y0;

for i = 1:length(t)-1
    w(i+1) = w(i) + step*func(t(i),w(i));  
end

vals = w;
end

