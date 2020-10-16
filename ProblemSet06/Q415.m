% Landon Buell
% 15 Oct 2020
% Hw 06
% Q 4.1.5 (Computer)



% Produce Raw Data
P = [0.59 0.8 0.95 0.45 0.79 0.99 0.9 0.65 0.79 0.69 0.79 0.49 1.09 0.95 0.79 0.65 0.45 0.6 0.89 0.79 0.99 0.85];
S = [3980 2200 1850 6100 2100 1700 2000 4200 2440 3300 2300 6000 1190 1960 2760 4330 6960 4160 1990 2860 1920 2160];

% PART A - Produce Demand Curve:
%   Fit function: S = c(1) + c(2)*P

% Build system matrix & Solve
A = [ones(size(P));P]';
left = A'*A;
right = A'*S';
c = linsolve(left,right)

% Compute RMSE
residualError = S' - A*c;
n = norm(residualError)


% MAx Selling profit:
Prof = (-9510 - 0.23) / (2*-8314)

