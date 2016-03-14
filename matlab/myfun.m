function f = myfun(x)
%{
sigma = [0.00324625, 0.00022983, 0.00420395; 0.00022983, 0.00049937, 0.00019247; 0.00420395, 0.00019247, 0.00764097];
q = 1000
beta = 0.9
mu = [0.0101110, 0.0043532, 0.0137058];

%rng default  % For reproducibility
r = mvnrnd(mu,sigma,q);
disp(r)
%}

f = x(1)*x(1) + x(2)*x(2) +x(3)*x(3)+x(4)