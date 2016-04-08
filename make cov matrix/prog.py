from math import sqrt
import glob
import time

def E(mas):
        return reduce(lambda x, y: x + y, mas) / len(mas)

def cov(x,y):

        E1 = E(x)
        E2 = E(y)
        new_mas = []
        size = min(len(x),len(y))
        for i in range(size):
                new_mas.append( (x[i] - E1)*(y[i]-E2) )
        
        return E(new_mas)



def check_date(date,dates):
        for i in range(len(dates)):
                if not date in dates[i]:
                        return False
        return True

def create_mas():
        values = []
        dates = []
        count = 0
        for file in glob.glob("stocks/*.txt"):
                count +=1
                f = open(file, "r")
                temp_val = []
                temp_dat = []
                for s in f:
                        if "<" in s:
                                continue

                        temp_val.append(float(s.split(',')[-1][:-1]))
                        temp_dat.append(int(s.split(',')[2]))

                values.append(temp_val)
                dates.append(temp_dat)
                
                f.close()
        return values,dates

def toprofit(values):
        for i in range(len(values)):
                for k in range(len(values[i])-1):
                        k+=1
                        values[i][k]=values[i][k]-values[i][k-1]
                values[i][0] = values[i][1]

        return values

def sync_mas(values,dates):
        values = toprofit(values)

        
        new_values=[[] for i in range(len(values))]
        for number in range(len(values)):
                for i in range(len(dates[number])):
                        if not check_date(dates[number][i],dates):
                                #print dates[number][i]
                                pass

        return values


def create_cov_matr(values):
        matr = [[0 for i in range(len(values))] for k in range(len(values))]
        
        for i in range(len(values)):
                for j in range(len(values)):
                        matr[i][j] = cov(values[i],values[j])
        return matr
def create_mean_return(values):
        a=[E(i) for i in values]
        return a
def create_file(x):
        k=[]
        for i in range(count):
                k.append(len(x[i]))
                         
        len1 = min(k)
        print len1
        f = open("values.txt",'w')
        for i in range(len1):
                st=''
                for k in range(count):
                        st+=str(x[k][i])+' '

                f.write(st[:-1]+'\n')
        f.close()
        
def print_matr(matr):
        for i in range(len(matr)):
                       print matr[i]
def tostring(mas):
        ans=''
        for i in mas:
                ans+=str(i)+' '
        return ans
def write_in_file(cov_matr, mean_list):
        f_matr = open("matr.txt","w")
        f_list = open("mean.txt","w")
        f_list.write(tostring(mean_list))
        for i in range(len(cov_matr)):
                f_matr.write(tostring(cov_matr[i]))
                f_matr.write('\n')

        f_list.close()
        f_matr.close()
cov_matr = create_cov_matr(sync_mas(*create_mas()))
mean_mas = create_mean_return(create_mas()[0])                  
print "MATR"
print_matr(cov_matr)
print "MEAN"
print mean_mas

write_in_file (cov_matr, mean_mas)
'''

print create_mean_return(create_mas()[0])
values = create_mas()[0][3]
for i in values:
        print i- E(values)

print E(values)
for i in values:
        
        mas.append((i-E(values))*(i-E(values)))

min_range = 0
for number in range(count):
        for ind in range(len(dates)):
                if dates[number][
        


from math import sqrt
x = [24,27,26,21,20,31,26,22,20,18,30,29,24,26]
y = [100,115,117,119,134,94,105,103,111,124,122,109,110,86]

print len(x),len(y)

def E(x):
        sum1 = 0.0
        for i in x:
                sum1+=i
        return sum1/len(x)
print E(x),E(y)

def cor(x,y):
        sum1 = 0.0
        sum2 = 0.0
        sum3 =0.0
        E1 = E(x)
        E2 = E(y)
        for i in range(len(x)):
                sum1+=(x[i] - E1)*(y[i]-E2)
                sum2+=(x[i]-E1)*(x[i]-E1)
                sum3+=(y[i]-E2)*(y[i]-E2)
        
        return sum1/sqrt(sum2*sum3)
print cor(x,y)
                
                
'''
