function root = NewtonsMethod(f,df,x0,n_steps)
%NewtonsMethod Computes Root of func
%   given function, derivative, guess, steps

x(1) = x0;

for i = 1:n_steps
    x(i+1) = x(i) - f(x(i))/df(x(i));
end


root = x(i+1);
end

