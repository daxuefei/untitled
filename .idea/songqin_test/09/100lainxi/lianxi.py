#---------------------练习98
# import os
# os.chdir('C:\\Users\\Administrator\\Desktop')
# with open('test5.txt','w',encoding='utf8') as f:
#     s=input('请输入字符串：')
#     s=s.upper()
#     f.write(s)
#-----------------------练习97
# import os
# # import stdout
# os.chdir('C:\\Users\\Administrator\\Desktop')
# with open('test1.txt','w',encoding='utf8') as f:
#     s=input('请输入字符串：\n')
#     while s != '#':
#         f.write(s)
#         # stdout.write(s)
#         s=input('')

    # f.write(str(d))
#--------------
# import os
# os.chdir('C:\\Users\\Administrator\\Desktop')
# if __name__ == '__main__':
#     from sys import stdout
#     filename = input('输入文件名:\n')
#     fp = open(filename,"w")
#     ch = input('输入字符串:\n')
#     while ch != '#':
#         fp.write(ch)
#         stdout.write(ch)
#         ch = input('')
#     fp.close()

#------------------------------map函数
# def normalize(name):
#      return name[0:1].upper()+name[1:].lower()
#
#
# list2 = list(map(normalize,['adam','LISA','barT']))
# print(list2)

#-----------------map&reduce函数
#作用：把字符串变成整数类型
# from functools import reduce
# DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}
#‘把字符串变成整数类型’
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num,s))

#---简化上述代码
# def char2num(s):
#     return DIGITS[s]
# def str2int(s):
#     return reduce(lambda x,y:x*10+y,map(char2num,s))
#
# print(str2int('12345'))
# print(type(str2int('12345')))


#----------------------把字符串变成浮点数(未完成)
# def str2float(s):
#     s1,s2 = s.split('.')
#     print(s1)
#     print(s2)
#     def gn(x,y):
#         return x*10+y
#     def fn(x,y):
#         return x/10+y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(gn,map(char2num,s1))+reduce(fn,map(char2num,s2))
#
# print(str2float('12.45'))

#----------计算字符串中字串出现的次数
# str1=input('请输入一个字符串：')
# str2=input('请输入一个子字符串：')
# ncount=str1.count(str2,2,9)
# print(ncount)


#-------------------练习95
# from dateutil import parser
# dt=parser.parse('Aug 28 2015 12:00AM')
# print(dt)


#------------------猜数字
# if __name__=='__main__':
#     import time
#     import random
#     play_it=input('do you want to play it.(\'y\' or \'n\')')
#     while play_it == 'y':
#         c = input('input a character:\n')
#         i = random.randint(0,2**32) %100
#         print('please input number your guess:\n')
#         start =time.clock()
#         # a=time.time()
#         guess = int(input('input your guess:\n'))
#         while guess !=i:
#             if guess > i:
#                 print('please inpuit a litter smaller')
#                 guess = int(input('please input your guess：\n'))
#             else:
#                 print('please input a big guess')
#                 guess=int(input('please input your guess:\n'))
#         end=time.clock()
#         # b=time.time()
#         var = (end-start) /18.2
#         print(var)
#
#         if var <15:
#             print('you are very clever!')
#         elif var <25:
#             print('you are normal!')
#         else:
#             print('you are stupid!!')
#         print('Congradulations')
#         print('The number you guess is %d' % i)
#         play_it=input('do you want to paly it')






























#--------------