function [val] = CompositeTrapezoid(f,a,b,m)
%Composite Trapezoid
%   Integrate "func" from a to b w/ Comp-Trap method

x = linspace(a,b,m);
h = x(2) - x(1);

y0 = f(a);
ym = f(b);
sum = 0;
for i = 1:m-1
    sum = sum + f(x(i));
end
val = h/2 * (y0 + ym + 2*sum);
end

