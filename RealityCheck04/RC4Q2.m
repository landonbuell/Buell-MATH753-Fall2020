% Landon Buell
% Marc Lyon
% MATH 753.01 - RC4
% 24 October 2020

c = 3e5;

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

% Define Functions - F(r) w/ r = r(x,y,z,d)
F1 = @(r)   (r(1)-A(1))^2 + (r(2)-B(1))^2 + (r(3)-C(1))^2 - (c*(t(1)-r(4)))^2;
F2 = @(r)   (r(1)-A(2))^2 + (r(2)-B(2))^2 + (r(3)-C(2))^2 - (c*(t(2)-r(4)))^2;
F3 = @(r)   (r(1)-A(3))^2 + (r(2)-B(3))^2 + (r(3)-C(3))^2 - (c*(t(3)-r(4)))^2;
F4 = @(r)   (r(1)-A(4))^2 + (r(2)-B(4))^2 + (r(3)-C(4))^2 - (c*(t(4)-r(4)))^2; 
                
        
F = @(r) F1 - F2 - F3 - F4;

