% Landon Buell
% MATH 753.01 - HW05
% Q 3.1.17
% 4 Oct 2020

% Create array of coeffs for ease of writing
C = [280,0.06,0.001,1.6e-5];
P = @(x) C(1) + C(2)*(x-1800) + C(3)*(x-1800)*(x-1850) + C(4)*(x-1800)*(x-1850)*(x-1900);

P(1950)
P(2050)
