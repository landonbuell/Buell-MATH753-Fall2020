% Landon Buell
% Mark Lyon
% MATH 753 - HW06
% 12 oct 2020

% Define Hypothesis-space function handles
F3 = @(t) [1 , cos(2*pi*t) , sin(2*pi*t)];
F4 = @(t) [1 , cos(2*pi*t) , sin(2*pi*t) , cos(4*pi*t)];

% Define input/output vectors
t = [0 ; 1/6 ; 2/6 ; 3/6 ; 4/6 ; 5/6];
b = [4 ; 2 ; 0 ; -5 ; -1 ; 3];

% Create Matrix A for F3
A = [];     % empty matrix
for i = 1:size(t)
    A = [A;F3(t(i))];
end
    
% Solve the system w/ F3
left = A' * A;
right = A' * b;
F3solution = linsolve(left,right)

% Find Error w/ F3 Solution
errorVector = A * F3solution - b;
F3error = norm(errorVector)

% Create Matrix A for F4
A = [];     % empty matrix
for i = 1:size(t)
    A = [A;F4(t(i))];
end
    
% Solve the system w/ F4
left = A' * A;
right = A' * b;
F4solution = linsolve(left,right)

% Find Error w/ F4 Solution
errorVector = A * F4solution - b;
F4error = norm(errorVector)