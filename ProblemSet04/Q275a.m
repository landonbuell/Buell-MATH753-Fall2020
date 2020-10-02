% Landon Buell
% Sauer 2.7.2 (Computer problem)

% Define system matrix
F = @(x) [  (x(1)-1)^2+(x(2)-1)^2+(x(3)-0)^2 ;
            (x(1)-1)^2+(x(2)-0)^2+(x(3)-1)^2 ;
            (x(1)-0)^2+(x(2)-1)^2+(x(3)-1)^2 ];

% Define Jacobian Matrix
DF = @(x) [ 2*x(1)-2 2*x(1)-2 2*x(3) ; 
            2*x(1)-2 2*x(1) 2*x(3)-2 ;
            2*x(1) 2*x(1)-2 2*x(3)-2 ];
        
% Solve Netwon's method w/ systems
x0 = [0;0;0];
sol = MulitvariateNewton(F,DF,x0,100);
disp(sol)