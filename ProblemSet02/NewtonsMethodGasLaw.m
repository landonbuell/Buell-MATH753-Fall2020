function root = NewtonsMethodGasLaw(x0,n_steps)
%NewtonsMethod Computes Root of func
%   given function, derivative, guess, steps

x(1) = x0;
% Establish constants
P = 20;
T = 700;
R = 0.0820578;
n = 1;
a = 18.0;
b = 0.1154;

% Define Van Der Waal Equation
f = @(x) (P + (n^2 * a)/x^2) * (x - n*b) - n*R*T;
df = @(x) -n^2*a*(x^-2) + 2*n^3*a*b*(x^-3) + P;
for i = 1:n_steps
    x(i+1) = x(i) - f(x(i))/df(x(i));
end


root = x(i+1);
end

