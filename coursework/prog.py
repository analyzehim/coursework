import numpy as np
import time

m = [0.0101110, 0.0043532, 0.0137058]
V = [[0.00324625, 0.00022983, 0.00420395],
     [0.00022983, 0.00049937, 0.00019247],
     [0.00420395, 0.00019247, 0.00764097]]
q = 1000
beta = 0.9


def generate_y():
        y = np.random.multivariate_normal(m, V, q)
        return y

def F_beta(x,alpha):
        ans = 0.0
        ans += alpha
        sum_loss = 0.0
        y = generate_y()
        for i in range(q):
                loss = (-1) * x.dot(y[i]) - alpha
                if loss > 0:
                        sum_loss += loss
        sum_loss/=(q*(1-beta))
        ans+=sum_loss
        return ans


def F_minimize():
        alpha = 0.06795
        F_beta_min = 1
        x1 =0.0
        x2 = 0.0
        x3 = 0.0
        for a in range(10000):
                for b in range(10000):
                        x1 = float(a)/10000
                        x2 = float(b)/10000
                        if x1+x2>0.5:
                                continue
                        x3 = 1- x1 -x2
                        f_b = F_beta(np.array([x1, x2, x3]), alpha)
                        if f_b < F_beta_min:
                                F_beta_min = f_b
                                print F_beta_min,"x: ",x1,x2,x3
        return F_beta_min

time1 = time.time()
print F_beta(np.array([0.35250, 0.15382, 0.49368]), 0.06795)
print time.time() - time1

        

        
