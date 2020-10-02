% Landon Buell
% Mark Lyon
% MATH 753 - HW04
% 20 Sept 2020

n = 500;
A = diag(sqrt(1:n)) + diag(cos(1:(n-10)),10) + diag(cos(1:(n-10)),-10);
x = ones(n,1);