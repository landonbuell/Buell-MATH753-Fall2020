function root = BroydenMethodI(f,x0,k)
% BroydenMethod II uses Broyden's Method v2 to find roots of equations
% A - System matrix to solve
% x0 - Initial Guess
% k - Maximum number of steps
[n,m] = size(x0);
A = eye(n,n);           % Intiali A matrix
for i = 1:k
    x = x0 - inv(A) * f(x0);
    del = x - x0;
    Del = f(x) - f(x0);
    A = A + (Del - A * del) * del' / (del' * del);
    x0 = x;
    disp(x0);
end

