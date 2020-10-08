% Landon Buell
% MATH 753.01 - HW05
% Q 3.2.2 - Computer
% 4 Oct 2020

x = linspace(-2*pi,+2*pi,1000);

for j=1:length(x)
    sf(j)=sin1(x(j));
end

error = sin(x) - sf;

plot(error)
