% Landon Buell
% 15 Oct 2020
% Hw 06
% Q 4.2.6 (Computer)



% Produce Raw Data
t = [1,2,3,4,5,6,7,8,9,10];
x = [6.2 9.5 12.3 13.9 14.6 13.5 13.3 12.7 12.4 11.9];

% Construct A & b
A = [ones(size(t));log(t)]';
b = log(x)'-log(t)';

% Left & right sizes, solve
left = A'*A;
right = A'*b;
c = linsolve(left,right)