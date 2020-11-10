function [vals] = TrapezoidMethod(func,t,y0)
%TrapezoidMethod Solve 1st order ODE with Trapezoidal method
% func : right side of eqn
% t : time axis
% y0 : starting function value
% step : step size 

step = t(2) - t(1);
w = zeros(size(t));
w(1) = y0;

for i = 1:length(t)-1
    f1 = func(t(i),w(i));
    f2 = func(t(i) + step , w(i) + step*f1);
    w(i+1) =  w(i) + (step/2)*(f1 + f2);
end

vals = w;
end

