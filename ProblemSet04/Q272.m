% Landon Buell
% Mark Lyon
% MATH 753 - HW04
% 20 Sept 2020

% System matrix
F = @(x) [  6*x(1)^3+x(1)*x(2)-3*x(2)^3-4 ;
            x(1)^2-18*x(1)*x(2)^2+16*x(2)^3+1 ];
        
% Jacobian matrix
DF = @(x) [ 18*x(1)^2+x(2) , x(1)-9*x(2)^2 ;
            2*x(1)-18*x(2)^2 , -36*x(1)*x(2)+48*x(2)^2 ];
        
k = 100;
% Solve w/ Newtons Method
x0 = [ 2; 2 ];
root = MultivariateNewton(F,DF,x0,k)

% Solve w/ Newtons Method
x0 = [ -1; -1 ];
root = MultivariateNewton(F,DF,x0,k)

% Solve w/ Newtons Method
x0 = [ =1 ; 1 ];
root = MultivariateNewton(F,DF,x0,k)