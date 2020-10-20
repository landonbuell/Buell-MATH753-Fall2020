function [val,err1,err2] = ThreePointCenteredDifference(f,d4f,x,h)
%ThreePointCenteredDifference (f,x,h)
%   Compute Approximation of second derivative of f at x w step h

val = (f(x-h) - 2*f(x) + f(x+h)) / h^2;
err1 = (h^2/12) * d4f(x);
err2 = (h^2/12) * d4f(x+h);

end

