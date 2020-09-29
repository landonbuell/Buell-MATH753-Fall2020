function root = BroydenMethodII(f,x0,k)
% BroydenMethod II uses Broyden's Method v2 to find roots of equations
% f - Function system to solve
% x0 - Initial Guess
% k - Maximum number of steps
[n,m] = size(x0);
b = eye(n,n);           % Intiali B matrix
for i = 1:k
    x = x0 - b * f(x0);
    del = x - x0;
    Del = f(x) - f(x0);
    b = b + (del - b * Del) * del' * b / (del' * b * Del);
    x0 = x;
    disp(x0);
end

