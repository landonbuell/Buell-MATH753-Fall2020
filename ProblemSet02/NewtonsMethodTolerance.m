function root = NewtonsMethodTolerance(f,df,x0,tol)
%NewtonsMethod Computes Root of func to tolerance
%   given function, derivative, guess, steps

x(1) = x0;
i = 1;
while x(i) - f(x(i))/df(x(i)) > tol
    x(i+1) = x(i) - f(x(i))/df(x(i));
    i = i + 1;
end

root = x(i+1);
end


