function f = Fbeta(x)

sigma = [0.00324625, 0.00022983, 0.00420395; 0.00022983, 0.00049937, 0.00019247; 0.00420395, 0.00019247, 0.00764097];
q = 20000;
beta = 0.99;
mu = [0.0101110, 0.0043532, 0.0137058];
y = mvnrnd(mu,sigma,q);
alpha = x(4);
x_vec=x(1:3);
ans = alpha;
sum_loss = 0.0;

for i = 1:q
    res = x_vec * transpose(y(i,:));
    loss = (-1)* res - alpha;
    if loss >0
        sum_loss = sum_loss + loss;
    end
end
sum_loss = sum_loss/(q*(1-beta));
ans = ans+ sum_loss;

f = ans;