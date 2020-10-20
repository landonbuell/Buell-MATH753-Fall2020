function [val,err] = ThreePointCenteredDifference2ndDeriv(f,d4f,x,h)
%ThreePointCenteredDifference (f,x,h)
%   Compute Approximation of scond derivative of f at x w/ step h
%   Compute accompaying error as well

val = (f(x-h) - 2*f(x) + f(x+h))/(h^2);
err = (h^2/12) * d4f(x);

end

