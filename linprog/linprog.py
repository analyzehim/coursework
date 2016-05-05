from scipy.optimize import linprog
import numpy as np
import time


def F_beta(x,y):

    ans = 0.0
    alpha = x[-1]
    ans += alpha
    sum_loss = 0.0
    for i in range(q):
                loss = (-1) * x[:-1].dot(y[i]) - alpha
                if loss > 0:
                        sum_loss += loss
    sum_loss/=(q*(1-BETA))
    ans+=sum_loss
    return ans

def print_mat(A):
        for i in A:
                print i



def gen_multimormally():
        q = 1000
        f = open("1/mean.txt","r")
        for i in f:
                m = [float(x) for x in i.split(',')]
        f.close()
        
        f = open("1/cov.txt","r")
        V=[]
        for i in f:
                V.append([float(x) for x in i.split(',')])
        f.close()

        VARS = len(m)
        y = np.random.multivariate_normal(m, V, q).tolist()
        return q,y,VARS

def gen_empirically():
     f = open("stocks.txt","r")
     y=[]
     for i in f:
                y.append([float(x) for x in i[1:-2].split(',')])
     q = len(y)
     VARS = len(y[0])
     f.close()
     return q,y,VARS

def bounders_generate():
        I = np.eye(q).tolist()

        func = [0 for i in range(VARS)] + [1] + [1.0/(q*(1-BETA)) for i in range(q)]

        A_eq = [[1 for i in range(VARS)] + [0]+[0 for i in range(q)],[0 for i in range(VARS+q+1)]]
        b_eq = [1,0]

        A_ub = [ [-x for x in y[i]] +[-1] + [-x for x in I[i]] for i in range(q)]
        b_ub=[0 for i in range(q)]

        bounds=((0,1),)
        for i in range(VARS-1):
                bounds+=((0,1),)

        for i in range(q+1):
                bounds+=((0,None),)
        return func, A_ub, b_ub, A_eq, b_eq, bounds


BETA = 0.9
q,y,VARS = gen_empirically()


res = linprog(*bounders_generate())

print "Function: ", res.fun
print "alpha: ", res.x[3]
print "x: ", res.x[0:3]
x=[]
for i in range(VARS+1):
        x.append(res.x[i])
x= np.array(x)
print "Error: ", F_beta(x,y) - res.fun
