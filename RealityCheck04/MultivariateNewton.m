function [root] = MultivariateNewton (F,J,r0,k)
%MulitvariateNetwon - Solve Multivariate system
%   F - Function handle to solve
%   J - Jacobian for Function handel
%   r0 - initial guess

for i = 1:k   
    s = linsolve(J(r0),F(r0));
    r1 = r0 - s;   
    r0 = r1;
end
root = r0;
end

