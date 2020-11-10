function [vals] = RungeKutta4(func,t,y0)
%RungKutta Solve 1st order ODE with Runge-Kutta 4-th order Method
% func : right side of eqn
% t : time axis
% y0 : starting function value
% step : step size 

step = t(2) - t(1);
w = zeros(size(t));
w(1) = y0;

for i = 1:length(t)-1
    % Compute s1 , s2 , s3 , s4
    s1 = func(t(i),w(i));
    s2 = func(t(i) + (step/2) , w(i) + (step/2)*s1);
    s3 = func(t(i) + (step/2) , w(i) + (step/2)*s2);
    s4 = func(t(i) + step , w(i) + step*s3);
    % apply update
    w(i+1) = w(i) + (step/6) * (s1 + 2*s2 + 2*s3 + s4);
    
end

vals = w;
end

