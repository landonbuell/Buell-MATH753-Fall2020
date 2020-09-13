function fixedPoint = FixedPointIteration(func,x0,n_steps)
%FixedPointIteration compute where g(x) = x
   % Compute where g(x) = x given function and number of steps
x(1) = x0;

% Iterate
for i = 1:n_steps
    x(i+1) = func(x(i));
end

%return fixed point
fixedPoint = x(n_steps+1);

end

