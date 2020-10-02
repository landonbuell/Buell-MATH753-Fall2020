function root = MulitvariateNewton(F,DF,x0,k)
%MulivariateNetwon uses Multivariate Newton's method to solve the system
% F - System matrix
% DF - Jacobian matrix
% x0 - Initial Guess
% k - number of iterations

for i = 1:k
    
    s = DF(x0)\F(x0);
    x1 = x0 + s;
    x0 = x1;

end
root = x0;

end
