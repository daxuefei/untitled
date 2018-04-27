#高阶函数
# def add(x,y,f):
#     return f(x) + f(y)
# print(add(-5,6,abs))



#生成器
#----------------------------------
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# print(fib(7))
#----------------------------------
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield (3)
#     print('step 3')
#     yield(5)
#
# o=odd()
# print(next(o))
# print(next(o))

#map函数:map将传入烦人函数依次作用到序列的每一个元素，并把结果作为新的Iterator（迭代器）返回
# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5])
# print(list(r))
#--------------------------------

#reduce函数,reduce把一个函数作用在一个序列[x1,x2,x3,x4.......]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# from functools import reduce
# def add(x,y):
#     return x+y
# print(reduce(add,[1,3,5,7,9]))

#----------------map练习
# def normalize(names):
#     return names.capitalize()#capitalize()函数返回首字符是大写的字符串
# name=map(normalize,['adma','LISA','barT'])
# print(list(name))
#----------------------reduce练习
# from functools import reduce
# def prod(x,y):
#     return x*y
#
# print(reduce(prod,[1,2,3,4,5,6]))

#---------------------------
#filter()函数，用于过滤器序列，根据返回值是Ture还是false决定保留还是丢弃该元素




#-------------------------------
# def by_name(t):
#     return sorted(t)
# r=map(by_name([('BOb',75),('Adam','92'),('Bart',66),['Lisa',88]]))
# print(list(r))

#------------------------------------返回函数
#函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_s
# um返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax = ax+n
#
#         return ax
#     return sum
#
# f=lazy_sum(1,3,5,7,9)
# print(f)
# print(f())

#---------------------------------------------------
#结果都是9，原因在于返回的函数引用了变量i，但它并非立即执行的，等到3个函数都返回时，他们引用的变量i已经变成了3，因此结果为9
#记住：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3=count()
# print(f1(),f2(),f3())

#------------------------------------------------------修改代码
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs
# f1,f2,f3=count()
# print(f1(),f2(),f3())

#----------------------------------------\
# list=list(map(lambda x:x*x,[1,2,3,4,5,6]))
# print(list)


#------------------------------匿名函数
# def build(x,y):
#     return lambda:x*x+y*y
# r=build(1,2)
# print(r())


#----------------------装饰器
#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# def now():
#     print('2015-3-25')
# f = now()
# print(now.__name__)
# print(f.__name__)
#---------------------------
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():'% func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-15')
# now()

#------------------------------------------
# import functools
# import time

# def metric(func):
#     @functools.wraps(func)
#     def now_time(*args,**kw):
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         # print(stop_time)
#         # return func(*args,**kw)
#         print('The running time is{}'.format(start_time - stop_time))
#     return now_time


#------------------------------------------------------
# class Student(object):
#
#     def __init__(self,name,score):
#         self.name = name
#         self.score =score
#
# bart = Student('Bart Simpson',59)
# # print(bart.name)
# # print(bart.score)
#
# #--------------------------------------------------------
# def print_score(std):
#     print('%s:%s' %(std.name,std.score))
#
# print(print_score(bart))

































