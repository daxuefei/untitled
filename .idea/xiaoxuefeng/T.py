#-----------------------TCP编程
from functools import reduce
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}
s='123.45'
s1,s2=s.split('.')
print(type(s2))
def gn(x,y):
    return x*10+y
def fn(x,y):
    return x/10+y
def char2num(s):
    return DIGITS[s]
r=reduce(gn,map(char2num,s1))+reduce(fn,map(char2num,int(s2)/100))

print(r)
