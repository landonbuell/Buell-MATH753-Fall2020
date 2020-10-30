function [value] = GaussianQuadrature(func)
%GaussianQuadrature Integrate 'func' on interval [a,b] using N steps

% Define Constants
x = [-0.86113631159405,-0.33998104358486,0.33998104358486,0.86113631159405];
c = [0.34785484513745,0.65214515486255,0.65214515486255,0.34785484513745];

% Compute sum
value = 0;
for i = 1:4
    newVal = c(i)*func(x(i));
    value = value + newVal;
end

