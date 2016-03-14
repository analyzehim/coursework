%fmincon(fun,x0,A,b,Aeq,beq,lb,ub)

v = [0.35250 0.15382 0.49368 0.06795];
disp('_______________________________')
disp('Begin')
global cons;
cons = 2;
%[x,fval] = fmincon(@myfun,v,[0 0 0 0],0,[1 1 1 0],1, [0 0 0 0], [1 1 1 100]);

disp(Fbeta(v))
%disp('f = ')
%disp (fval)
%disp ('x')
%disp(x)
