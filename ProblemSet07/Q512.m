% Landon Buell
% Mark Lyon
% MATH 753.01 - HW07
% 20 Oct 2020

% Set Function & derivative
f = @(x) 1/(1+x);
d3f = @(x) -6/(1+x)^4;

% Create a list of h's (steps) to use and evaluation pt:
exps = -linspace(1,10,10);
steps = (10.^exps)';
x0 = 1;

% Loop through stepsizes and store values:
for i = 1:size(steps)
    [val,err] = ThreePointCenteredDifference(f,d3f,x0,steps(i));
    errors(i) = err;
end

% Plot Just Errors at each step
plot(errors)

