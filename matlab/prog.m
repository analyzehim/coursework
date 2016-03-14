%fmincon(fun,x0,A,b,Aeq,beq,lb,ub)

% This is example v = [0.35250 0.15382 0.49368 0.06795];
disp('_______________________________')
disp('Begin')
[x,fval] = fmincon(@Fbeta,v,[0 0 0 0],0,[1 1 1 0],1, [0.0001 0.0001 0.0001 0.01], [1 1 1 100]);

disp('f = ')
disp (fval)
disp ('x')
disp(x)
