function [val] = CompositeSimpson(f,a,b,m)
%Composite Trapezoid
%   Integrate "func" from a to b w/ Comp-Trap method

x = linspace(a,b,2*m);
h = x(2) - x(1);

y0 = f(a);
y2m = f(b);

sum1 = 0;
for i = 1:m
    sum1 = sum1 + f(x(2*i-1));
end
sum2 = 0;
for i = 1:m-1
    sum2 = sum2 + f(x(2*i));
end
val = (h/3)*(y0 + y2m + 4*sum1 + 2*sum2);
    
end

