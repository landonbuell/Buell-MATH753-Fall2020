% Landon Buell
% MATH 753.01 - HW05
% Q 3.1.8
% 4 Oct 2020

% Create L1 & L10 Coeffs
L1 = @(x,y) ((x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-10))/((y-2)*(y-3)*(y-4)*(y-5)*(y-6)*(y-7)*(y-8)*(y-9)*(y-10));
L10 = @(x,y) ((x-2)*(x-3)*(x-4)*(x-5)*(x-6)*(x-7)*(x-8)*(x-9)*(x-1))/((y-2)*(y-3)*(y-4)*(y-5)*(y-6)*(y-7)*(y-8)*(y-9)*(y-1));

% Output values
y1 = 122;
y10 = 2;

P = y1*L1(0,1) + y10*L10(0,10)