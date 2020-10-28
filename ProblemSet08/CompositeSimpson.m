function [val] = CompositeSimpson(f,a,b,m)
%Composite Trapezoid
%   Integrate "func" from a to b w/ Comp-Trap method

x = linspace(a,b,m);
h = x(2) - x(1);

sum = 0;
for i = 1:m
    w = x(i) + h/2;
    sum = sum + f(w);
end
val = h*sum;
end

