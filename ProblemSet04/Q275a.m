% Landon Buell
% Sauer 2.7.2 (Computer problem)

% Define system matrix
F = @(x) [  (x(1)-1)^2+(x(2)-1)^2+x(3)^2-1 ;
            (x(1)-1)^2+x(2)^2+(x(3)-1)^2-1 ;
             x(1)^2+(x(2)-1)^2+(x(3)-1)^2-1 ];

% Define Jacobian Matrix
DF = @(x) [ 2*x(1)-2 2*x(1)-2 2*x(3) ; 
            2*x(1)-2 2*x(1)   2*x(3)-2 ;
            2*x(1)   2*x(1)-2 2*x(3)-2 ];
        
% Solve Netwon's method w/ systems
x0 = [2,1,2];
sol = MultivariateNewton(F,DF,x0,100);
disp(sol)

% Solve Netwon's method w/ systems
x0 = [1/2;1/2;1/2];
sol = MultivariateNewton(F,DF,x0,100);
disp(sol)