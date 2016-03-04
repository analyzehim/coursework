import random
import time
q = 1000
beta = 0.9
def generate_sample():
        while True:
                y1 = float(random.randint(1,10000))/10000
                y2 = float(random.randint(1,10000))/10000
                y3 = 1 - y1 - y2
                if y3>0:
                        break

        return (y1,y2,y3)

def generate_y():
        y=[]
        for i in range(q):
                y_sample = generate_sample()
                y.append( y_sample )
        return y

def F_beta(x,alpha):
        ans = 0
        ans+=alpha
        for i in range(q):
                loss = 
time1 = time.time()
y = generate_y()
print time.time() - time1

        

        
