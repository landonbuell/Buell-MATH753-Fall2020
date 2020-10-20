function [val,err] = ThreePointCenteredDifference(f,d3f,x,h)
%ThreePointCenteredDifference (f,x,h)
%   Compute Approximation of first derivative of f at x w/ step h
%   Compute accompaying error as well

val = (f(x-h) - f(x+h))/(2*h);
err = (h^2/6) * d3f(x);

end

