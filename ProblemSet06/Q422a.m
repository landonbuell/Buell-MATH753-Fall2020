% Landon Buell
% Mark Lyon
% MATH 753 - HW06
% 12 oct 2020

% Define Hypothesis-space function handles
F3 = @(t) [1 , cos(2*pi*t) , sin(2*pi*t)];
F4 = @(t) [1 , cos(2*pi*t) , sin(2*pi*t) , cos(4*pi*t)];

% Define input/output vectors
t = [0 ; 1/6 ; 2/6 ; 3/6 ; 4/6 ; 5/6]';
b = [0 ; 2 ; 0 ; -1 ; 0 ; 0];

% Create Matrix A
A = F3(t)
