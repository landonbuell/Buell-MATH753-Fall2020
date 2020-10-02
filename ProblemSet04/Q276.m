% Landon Buell
% Sauer 2.7.6 (Computer problem)

% Define system matrix
F = @(x) [ (x(1)-1)^2+(x(2))^2+(x(3)-1)^2-8;
           (x(1))^2+(x(2)-2)^2+(x(3)-2)^2-2;
           (x(1))^2+(x(2)-3)^2+(x(3)-3)^2-2 ];

% Define Jacobian Matrix
DF = @(x) [ 2*x(1)-2 2*x(1) 2*x(3)-2 ; 
            2*x(1)   2*x(1)-2 2*x(3)-4 ;
            2*x(1)   2*x(1)-6 2*x(3)-6 ];
        
k = 100;
% Solve Netwon's method w/ systems
x0 = [1;1;1];
sol = MultivariateNewton(F,DF,x0,k);
disp(sol)
