# coding:utf-8
import xlrd
from xlwt import *
import os
import xlwt
import tablib


file=Workbook(encoding = 'utf-8')
table =file.add_sheet('aaa')
mysheet1=table.sheet_by_name("aaa")

#获取表的表头
titlelist=mysheet1.row_values(0)

data={
    "1":["张三",150,120,100],\
    "2":["wang",90,99,89],\
    "3":["wu",60,66,65]\
}
ldata=[]
num=[a for a in data]
num.sort()

for x in num:
    t= [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)

for i,p in enumerate(ldata):
    for j,q in enumerate(p):
        print(i,j,q)
        table.write(i,j,q)
file.save('aaa')