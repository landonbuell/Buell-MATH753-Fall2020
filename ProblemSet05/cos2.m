% Landon Buell
% MATH 753.01 - HW05
% Q 3.3.2 - Computer
% 4 Oct 2020

% Code below used in Sauer 3rd edition:
%Program 3.4 Building a sin calculator key, attempt #2
%Approximates sin curve with degree 9 polynomial
%Input: x
%Output: approximation for cos(x), correct to 10 decimal places
function y = cos2(x)
    %First calculate the interpolating polynomial and
    % store coefficients
    n = 10;
    b = pi/2+(pi/2)*cos((1:2:2*n-1)*pi/(2*n));  % for x in [0,pi/2]
    %b = (2e4)*cos((1:2:2*n-1)*pi/(2*n));    % for x in [-1e4,+1e4]
    yb = cos(b);                                % b holds Chebyshev base points
    c = newtdd(b,yb,n);
    %For each input x, move x to the fundamental domain and evaluate
    % the interpolating polynomial
    s = 1; % Correct the sign of cos
    x1 = mod(x,2*pi);
    if x1 > pi
        x1 = 2*pi-x1;
        s = -1;
    end
    if x1 > pi/2
        x1 = pi-x1;
    end
y = s*nest(n-1,c,x1,b);
end
        
        
        