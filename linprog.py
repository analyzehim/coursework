c = [1, 1 , -1]
A = [[-3, 1, 2], [1, 2, 3]]
b = [6, 4]
A_eq1 = [[1, 1, 1],[0,0,0]]
b_eq1 = [1,0]
x0_bounds = (0, 1)
x1_bounds = (0, 1)
x2_bounds = (0, 1)
from scipy.optimize import linprog
import numpy as np
import time
#res = linprog(c, A_ub=A, b_ub=b, A_eq = A_eq1, b_eq = b_eq1, bounds=(x0_bounds, x1_bounds,x2_bounds),options={"disp": True})
#print(res)


m = [0.0101110, 0.0043532, 0.0137058]
V = [[0.00324625, 0.00022983, 0.00420395],
     [0.00022983, 0.00049937, 0.00019247],
     [0.00420395, 0.00019247, 0.00764097]]
q = 1000
beta = 0.9
number_vars = q + 4
def generate_y():
        y = np.random.multivariate_normal(m, V, q)
        return y
def print_mat(A):
        for i in A:
                print i
        

I = np.eye(q).tolist()

func = [1,0,0,0]
func_z = [1.0/(q*(1-beta)) for i in range(q)]
func+=func_z

C_eq = [[0,1,1,1]+[0 for i in range(q)],[0 for i in range(number_vars)]]
d_eq = [1,0]

C_ub = [[-1] + [-x for x in generate_y()[0].tolist()] + [-x for x in I[i]] for i in range(q)]


d_ub=[0 for i in range(q)]

bounds1 = ((0,None),(0,1),(0,1),(0,1),)
for i in range(q):
        bounds1+=((0,None),)
'''
print "________ALL_________"
print "Func: ", func

print 'C_ub: '
print_mat(C_ub)
print 'd_ub: '
print_mat(d_ub)
print 'C_eq: '
print_mat(C_eq)
print 'd_eq: '
print_mat(d_eq)
print 'bounds: ', bounds1
print "______________"
'''

res = linprog(func, A_ub=C_ub, b_ub=d_ub, A_eq = C_eq, b_eq = d_eq,bounds = bounds1 ,options={"disp": False})
print res.x[0], res.x[1] + res.x[2] + res.x[3]
