function rt = BisectionAlgorithm(func,a,b,tol)
% BisectionAlgotithm
% Compute root of func between 'a' and 'b' to tolerance
% Detailed explanation goes here
if sign(func(a))*sign(func(b)) >= 0
    error("f(a)f(b) < 0 Not Met")
end

fa = func(a);
fb = func(b);
cntr = 0;

while (b - a) /2 > tol
    c = (a + b) / 2;
    fc = func(c);
    if fc == 0                  % This is solution!
        break
    end
    if sign(fc)*sign(fa) < 0   % a&c are new interval
        b = c ; fb = fc;
    else                        % b&c are new interval
        a = c ; fa = fc;    
    cntr = cntr + 1;
    end
end
disp(cntr)
rt = (a + b)/2 ;                 % best guess

