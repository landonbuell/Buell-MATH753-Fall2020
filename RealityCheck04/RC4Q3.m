% Landon Buell
% Marc Lyon
% MATH 753.01 - RC4
% 24 October 2020

%c = 3e5;

% Each col is either x,y,z
S = [   15600 , 7450 , 20140        
        18760, 2750 , 18610
        17610, 14630 , 13480
        19170 , 610 , 18390];
A = S(:,1);     % all x positions
B = S(:,2);     % all y positions
C = S(:,3);     % all z positions

% Set time intervals & initial guess
t = [0.07074 0.07220 0.07690 0.07242]';
r0 = [0 ; 0 ; 6370 ; 0];

syms c x y z d;

% Define Function - F(r) w/ r = r(x,y,z,d)
F = [   (x-A(1))^2 + (y-B(1))^2 + (z-C(1))^2 - (c*(t(1)-d))^2 == 0;
        (x-A(2))^2 + (y-B(2))^2 + (z-C(2))^2 - (c*(t(2)-d))^2 == 0;
        (x-A(3))^2 + (y-B(3))^2 + (z-C(3))^2 - (c*(t(3)-d))^2 == 0;
        (x-A(4))^2 + (y-B(4))^2 + (z-C(4))^2 - (c*(t(4)-d))^2 == 0]; 
    
% Use Symbolic Solver
Sol = solve(F,[x,y,z,d]);

% Evaluate at int. conds.
xSol = subs(Sol.x);
ySol = subs(Sol.y);
zSol = subs(Sol.z);
dSol = subs(Sol.d);
                
               

