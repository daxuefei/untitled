#练习1
# d=[]
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i !=j and j!=k and k!=i):
#                 d.append([i,j,k])
# print  ("总数量:",len(d))
# print (d)

#练习2
#encofing=utf-8

#
# profit(i)
# i=int(raw_input('请输入利润：'))

# i = int(input('净利润:'))
# if i <= 10:
#     j=i*0.1
# elif 10< i<=20:
#     j=10*0.1+(i-10)*0.075
# elif 20<i<= 40:
#     j=10*0.1+10*0.075+(i-20)*0.05
# elif 40<i<=60:
#     j=2.75+(i-40)*0.03
# elif 60<i<=100:
#     j=2.75+20*0.03+(i-60)*0.015
# elif i>100:
#     j=2.75+20*0.03+40*0.015+(i-100)*0.001
# else:
#     print('请输入大于0的数字')
# print(j)


#练习3
# for i in range(1,68):
#     for j in (1,68):
#         if i*j=168:
#             print(i "*" j "=168")

# def printme(str):
#     "打印任何传入的字符串"
#     print (str)
#     return;
#
# printme("我要调用用户自定义函数")

# def account_login():
#     password=input('password:')
#     if password == '12345':
#         print('Login success!')
#     else:
#         print('Wrong password or invalid input!')
#         account_login()
# account_login()

#定义函数
# def profit():
#     i = int(input('净利润:'))
#     if 0<i <= 10:
#         j=i*0.1
#     elif 10< i<=20:
#         j=10*0.1+(i-10)*0.075
#     elif 20<i<= 40:
#         j=10*0.1+10*0.075+(i-20)*0.05
#     elif 40<i<=60:
#         j=2.75+(i-40)*0.03
#     elif 60<i<=100:
#         j=2.75+20*0.03+(i-60)*0.015
#     elif i>100:
#         j=2.75+20*0.03+40*0.015+(i-100)*0.001
#     else:
#         print('请输入大于0的数字')
#         profit()
#     print(j)
#
#
# profit()

# #练习4
# year=input('请输入年份：\n')
# month=input('请输入月份：\n')
# day=input('请输入日期：\n')
# months1=[0,31,60,91,]

#练习5
# # d=[]
# i=input('请输入第一个数：')
# j=input('请输入第二个数：')
# k=input('请输入第三个数：')

# list=[i,j,k]
# print(sorted(list))


# print(sorted([int(input("enter a integer：")) for x in range(3)]))
# print(sorted([int(input("enter a integer: ")) for x in range(3)]))

# l=[i for i in input("enter 3 number:").split()]
# l.sort()
# print (l)

# print(sorted(i for i in input("enter 3 number:").split()))

#练习6
#使用递归
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print (fib(10))

#练习6 报错
# def fib(n):
#     a,b=1,1
#     for i in range(n-1):
#         a,b=b,a+b
#     return b
#  print (fib(10))

#练习7
# a=[1,2,3]
# b=a[:]
# print(b)


# l=[33,4,5,6,7]
# p=[]
# #遍历l中的每个元素
# for i in l:
#     p.append(i)
# print (p)


# a=[2,4,5,7]
# b=[]
# for i in range(len(a)):
#     b.append(a[i])
# print(b)

# a=[1,2,3,4,6]
# b=list()
# for i in a:b.append(i)
# print(b)

# #扩展
# a=[3,5,7]
# b=[]
# b.extend(a)
# print(b)


#练习8
# for i in range(1,10):
#     for j in range(1,10):
#         k=i*j
#         print("%d*%d=%d" % (i,j,k))


# for i in range(1,10):
#     print
#     for j in range(1,i+1):
#         # print(i,"*",j,"=",i*j)
#         # print ("%d*%d=%d" % (i,j,i*j))
#         print("{}*{}={}".format (i,j,i*j))


#练习9
# import time
# l=[1,2,3,7]
# for i in range(len(l)):
#     print (l[i])
#     time.sleep(1)

# import time
# i=1
# s=0
# if 0<i<10:
#
#     i+=1
#     s=s+i
# else:
#     pass
# print(i,s)
# time.sleep(1)

# import time
# i=1
# s=0
# while i<=10:
#     s =s+i
#     i=i+1
#     print (i)
#     time.sleep(1)
# print(s)

#练习11


#练习12
# a=[]
# for i in range(101,201):
#     for j in range(2,i-1):
#         if i%j ==0:
#             break
#     else:
#             a.append(i)
# print(len(a))
# print(a)

# l = []
# for i in range(101,200):
#     for j in range(2,i-1):
#         if i%j ==0:
#             break
#     else:
#         l.append(i)
#
# print(l)
#
# print("总数为：%d" % len(l))


#练习13
# for i in(100,1000):
#     a=i/100
#     b=i/10%10
#     c=i%10
#     if  i == a**3 + b**3 + c**3:
#         print(i)


# for n in range(100,1000):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print (n)


# for n in range(100,1000):
#     s=str(n)
#     a=s[0]
#     b=s[1]
#     c=s[2]
#     if s==int(a)**3+int(b)**3+int(c)**3:
#         print(s)



# print ([i for i in range(100,1000) if (i/100)**3+((i-i/100*100)/10)**3+(i%10)**3 == i])
#
# print (2**3)


#练习14 后面再看


#练习15
# sore=int(input("请输入分数："))
# if sore>=90:
#     grade='A'
# elif sore<=60:
#     grade='C'
# else:
#     grade='B'
#
# print("{}分属于等级{}".format(sore,grade))

# a=int(input('输入分数：'))
# print('A' if a>89 else('B' if a>59 else 'C'))

# i=int(input('请输入成绩：'))
# ar=[90,60,0]
# res=['A','B','C']
# for idx in range(0,3):
#     if i>=ar[idx]:
#         print(res[idx])
#         break


# import datetime
#
# if __name__ == '__main__':
#     #输出今天日期
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#
#
#     #创建日期对象
#     miyazakiBirthDate=datetime.date(1943,1,4)
#     print(miyazakiBirthDate.strftime('%d/%m/%Y'))
#
#     #日期算数运算
#     miyazakiBirthNextDay=miyazakiBirthDate+datetime.timedelta(days=2)
#     print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
#
#     #日期替换
#     miyazakiFirstBirthday=miyazakiBirthDate.replace(year=miyazakiBirthDate.year+1)
#     # miyazakiFirstBrithday=miyazakiBirthdate.replace(month=miyazakiBirthDate.month+2)
#     print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))



#获取日历上的时间
# import calendar
# cal =calendar.month(2018,2)
# print ("以下输出2018年2月日历：")
# print(cal)

#练习17
import string
# s=input('input string:\n')
# letters=0
# space=0
# digit=0
# other=0
# for i in s:
#     if i.isalpha():
#
#         letters +=1
#     elif i.isspace():
#         space +=1
#     elif i.isdigit():
#         digit +=1
#     else:
#         other +=1
# print("char={} space={} digit={} other={}".format(letters,space,digit,other))


#练习7
from functools import reduce
# Tn=0
# Sn=[]
# n=int(input('请输入相加的数字：'))
# a=int(input('请输入需要有几个数字相加：'))
# for count in range(n):
#     Tn=Tn+a
#     a=a*10
#     Sn.append(Tn)
#     print (Tn)
#
# # Sn =reduce(lambda x,y : x+y,Sn)
# Sn = reduce(lambda x,y : x + y,Sn)
# print('计算和为：',Sn)


#练习19（思考）
# for i in range(1,1001):
#     sum=0
#     for j in range(1,i):
#         if i % j==0:
#             sum+=j
#     if sum == i:
#         print(i)

#练习20
# tour=[]
# height=[]
#
# hei=100
# tim=10
#
# for i in range(1,tim+1):
#     if i==1:
#         tour.append(hei)
#     else:
#         tour.append(2*hei)
#     hei=hei/2
#     height.append(hei)
# print('总高度：',sum(tour))
# print('第10次返回高度：',hei)


# #升级为函数
# def height_fu(hei=100,time=10):
#     tour=[]
#     height=[]
#     for i in range(1,time+1):
#         if i==1:
#             tour.append(hei)
#         else:
#             tour.append(2*hei)
#         hei=hei/2
#     print('总高度{}'.format(sum(tour)))
#     print('第{}次返回高度{}'.format(time,hei))
# height_fu(200,10)


#练习21
# Fn=1
# Sn=[1]
# for i in range(9):
#     Fn=2*(Fn+1)
#     Sn.append(Fn)
# print(Sn[len(Sn)-1])
# print('一共摘了{}个桃子'.format(Sn[-1]))

# x=1
# for day in range(0.9):
#     x=(x+1)*2
# print(x)



#练习22
#方式1，移除不符合条件的数据
# l=[]
# k=[i+j for i in 'abc' for j in 'xyz']
# print(k)
# k.remove("ax")
# k.remove("ay")
# k.remove("by")
# k.remove("bz")
# k.remove("cx")
# k.remove("cz")
# print(k)

#方式2
# for i in range(ord('x'),ord('z')+1):
#     for j in range(ord('x'),ord('z')+1):
#         if i != j:
#             for k in range(ord('x'),ord('z')+1):
#                 if (i != j) and (j != k):
#                     if (i != ord('x')) and (k != ord('z')) and (k!=ord('x')):
#                         print('order is a--%s\t b--%s\t c--%s\t' % (chr(i),chr(j),chr(k)))
# #                         # print("a--{}".format(i))
# #                         # print("b--{}".format(j))
# #                         # print("c--{}".format(k))
#
#                           # print("a-{}b-{}c-{}".format(i,j,k) ))
#
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))

# for i in range(ord('x'),ord('z')+1):
#     for j in range(ord('x'),ord('z')+1):
#         if i != j:
#             for k in range(ord('x'),ord('z')+1):
#                 if (i != j) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k!=ord('z')):
#                         print ('order is a--%s\t b--%s\t c--%s\t' % (chr(i),chr(j),chr(k)))


#练习24
#方式1：while
# s=0
# n=1
# a=2
# b=1
# for n in range(1,21):
# while n <=20:
#     s=s+a / b
#     b,a=a,a+b
#     n+=1
#      # print(n)
#      # print(a,b)
# print(s)

#方式2 for
# a=2
# b=1
# s=0
# for n in range(1,21):
#     s=s+a/b
#     b,a=a,a+b
# print(s)

# def fib(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return int(fib(n-1)+fib(n-2))
# s=0
# for i in range(1,21):
#     s+=float(fib(i+2))/float(fib(i+1))
#     # print ("%s:%s%s" % (i,fib(i+2),fib(i+1)))
# print (s)

#练习25
# s=0
# t=1
# i=0
# for i in range(1,4):
#     t=i*t
#     s=s+t
# print(s)

# n = 0
# s = 0
# t = 1
# for n in range(1,4):
#     t *= n
#     s += t
# print(s)


# s=0
# def fib(n):
#     if n==1:
#         return n
#     else:
#         return n*fib(n-1)
#
# for n in range(1,21):
#     a=fib(n)
#     s+=a
# print(s)

#练习26
#递归函数
# def fib(n=5):
#     if n==1:
#         return n
#     else:
#         return n*fib(n-1)
#
# print(fib())


#练习27
# l=list(input('请输入5个字符：'))
# l.reverse()
# for i in range(len(l)):
#     print(l(i))

# S = input('Input a string:')
# L = list(S)
# L.reverse()
# for i in range(len(L)):
#     print(L[i])


# s=list(input('enter a string:'))
# s.reverse()
# # for i in range(len(s)):
# #     print(s[i])
# print(s)

#方式2
# def output(s,l):
#     if l==0:
#         return
#     print(s[l-1])#从后面打印元素
#     output(s,l-1)#调用函数
# s=input('entesr a string:')
# l=len(s)
# output(s,l)


#练习28
#自己设计的
# def fun(age,n):
#     if n==1:
#         return age
#     else:
#         return fun(age+2,n-1)
# print(fun(10,5))

#参考
# def age(n):
#     if n==1:c=10
#     else: c=age(n-1)+2
#     return c
# print(age(5))

#练习29
# k=[]
# k=input('enter a int:')
# l=list(k)
# # l=len(k)
# l.reverse()
# print('z这是{}位数'.format(len(l)))
# print((l))



# x='abdsyy'
# for i in range(len(x)-1,-1,-1):
#     print (x[i])

# #for循环
# for i in range(1,5):
#     print (i)
a=[1,23,4]
# for i in a[::-1]:
#     print (i)
# #
# l=[2,3,45,6]
# #顺序打印
# for i in range(len(l)):
#     print(l[i])
# #逆序打印
# for i in range(len(l)-1,-1,-1):
#     print(l[i])

#逆序打印
# a=[1,2,3]
# for i in a[::-1]:
#     print (i)

#join实例
# print ('\n'.join(['\t'.join(['%d * %d = %d'%(y,x,x*y) for y in range(1,x+1)])for x in range(1,10)]))

# str='-'
# seq=("a","b","c")
# print (str.join(seq))

#练习30
# l=int(input('enter a number:'))
# a=l/10000
# b=l/1000%10
# # c=l/100%10
# d=l%1000%100/10
# e=l%10
# if (a==e) and (b==d):
#     print(l)
# else:
#     print('此数不是回文数。')

# def is_true_num(num):
#     if 10000<=num and num <=99999:
#         b = num/10000
#         c = (num/1000)%10
#         d = (num%1000)%100/10
#         e = num%10
#         if (b==e and c==d):
#             print ("%d：是回文数"%num)
#         else:
#             print ("%d：不是回文数"%num)
#     else:
#         print ("%d：输入错误，请重新输入" % num)
# if __name__ == '__main__':
#     a = int(input("请输入5位数字："))
#     is_true_num(a)



# l=input('enter a number:')
# print(type(l))
# if l[0]==l[-1] and l[1]==l[-2]:
#     print("这个数是回文数字：%s" %  l)
# else:
#     print("这个数不是汇文数字:%s" % l)

#练习34
# def hello_word():
#     print ('hello world')
#
# def three_hellos():
#     for i in range(3):
#         hello_word()
# if __name__=='__main__':
#     three_hellos()

#练习35
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

# #练习36素数：只能被1和自己整除
# a=int(input('enter a number:'))
# for i in range(1,a):
#     if a/i==0:
#         break
# else:
#     print(a)

#正则表达式
# import re
# print(re.search('www','www.runoob.com').span())#在起始位置匹配

# import re
# line ="Cats are smarter than dogs"
# matchObj=re.match(r'(.*)are (.*?).*',line,re.M|re.I)
# if matchObj:
#     print("match.Obj.grooup():",matchObj.group())
#     print("match.Obj.group(1):",matchhObj.group(1))
#     print("match.Obj.group(2):",matchObj.group(2))
# else:
#     print("NO match")

#break
#实例1
# for letter in "Python":
#     if letter=='h':
#         break
#     print('当前字母：',letter)


#实例2
# var=10
# while var>0:
#     print('当前变量值：',var)
#     var=var-1
#     if var==5:
#         break
# print('Good bye!')
#contion
# for letter in "python":
#     if letter=="h":
#         continue
#     else:
#         print(letter)
# print('Good Bye')

#使用continu打印1~10里面的奇数
# for letter in range(1,11):
#     if letter%2==0:  #如果是偶数就继续执行
#         continue
#     else:
#         print(letter)

#pass语句
# for letter in "python":
#     if letter=="h":
#         pass
#         print('只是pass块')
#     print(letter)

#字典
# dictionary={}
# flag='a'
# pape='a'
# off='a'
# while flag=='a' or 'c':
#     flag=input('添加或查找单词？（a/c）')
#     if flag=='a':
#         word=input('输入单词（key）：')
#         defintion=input('输入定义值（value）：')
#         dictionary[str(word)]=str(defintion)
#         print('添加成功')
#         pape=input('您是否需要查找字典？（a/0）')
#         if pape==a:
#             print (dictionary)
#         else:
#             continue
#     elif flag=='c':
#         check_word




#练习100
# 列表转换成字典
#方式1
# i=['a','b']
# l=[1,2]
# print(dict([i,l]))

#方式2 为什么是逆序打印？
l1=[1,2,3,4,64]
l2=['aa','bb','cc','dd','ee']
d={}
for index in range(len(l1)):

    d[l1[index]]=l2[index]  #l1中的元素对应到l2中
print(d)

#######
# eee=[1,2,3,4,5]
# d={}
# d[2]=eee[4]
# print(d)

#方式2
# i=['a','b','c']
# l=[1,2,3]
# b=dict(zip(i,l))
# print(dict(zip(l,i)))

#方式4
# keys=['a','b']
# values=[1,2]
# print({keys[i]:values[i] for i in range(len(keys))})

#方式5
