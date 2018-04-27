
#定义一个判断手机号码是否是11位的函数，如果不是，重新输入
# def input_number():
#     iphone_number=input('请输入你的电话号码:')
#     if len(iphone_number) == 11:
#         print('输入的手机号码正确！正确的手机号码为：{}'.format(iphone_number))
#         nums = iphone_number[0:3]
#         print(nums)
#         if nums in ['134', '135','136','137','138','139','150','151','152','157','158','159','182','183','184','187','188','147','178']:
#             print('Operator:CN_mobile:{}'.format(iphone_number))
#         elif nums in ['130','131','132','155','156','185','186','145','176']:
#             print('Operator:CN_union:{}'.format(iphone_number))
#         elif nums in ['133','153','180','181','189','177']:
#             print('Operator：CN_telecon:{}'.format(iphone_number))
#         else:
#             print('输入的手机号码不对，请重新输入')
#             return input_number()
#
# input_number()




#字典推导式
# d={i:i+1 for i in range(4)}
# print(d)
# g = {i:j for i,j in zip(range(1,6),'abcde')}
# g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}

# print(g)


#词频统计

# path='C:\\Users\\Administrator\\Desktop\\Walden.txt'
# with open(path,'r',encoding="utf-8") as f:
#     words = f.read().split( )
#     print(words)
#     for word in words:
#         print('{}-{} times'.format(word,words.count(word)))



#升级词频统计
# import string
# path='C:\\Users\\Administrator\\Desktop\\Walden.txt'
# with open(path,'r',encoding="utf-8") as text:
#     words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
#     words_index=set(words)
#     counts_dict={index:words.count(index) for index in words_index}
#
# for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
#     print('{}--{} times'.format(word,counts_dict[word]))


#类__init__()
# class CocaCola():
#     formula = ['caffeine','sugar','water','soda']
#     def __init__(self,logo_name):
#         self.local_logo = logo_name
#         self.local_name = '可口可乐'
#
#         # for element in self.formula:
#         #     print('Coke has {}!'.format(element))
#
#     def drink(self):
#         print('Energy!')
#
# cock = CocaCola('哈哈')
# print(cock.local_logo)






#------------------------装饰器
# def foo():
#     print('foo')
#
# foo
# foo()

#----------------

# foo = lambda x: x + 1
#
# def foo():
#     print('foo')
#
#
#
#
# # print(foo(1))
# foo()

#----------
# def foo(func):
#     func()#调用bar()
#     print(type(func))
#
# def bar():
#     print("bar")
#
# foo(bar)

#-----------------------------
# var = 'var in global'
#
# def fun():
#     var = 'var in local'
#     print('fun:'+str(locals()))
#     # print(str(locals()))
#
# print('globals:'+str(globals()))
# fun()

#------------------------
# params_list=(1,2)
# params_tupple=(1,2)

# def add(x,y):
#     print(x+y)
#

# add(*params_list)
# print(type(add(*params_list)))
# add(*params_tupple)

#-------------------------
# params={
#     'x':1,
#     'y':2
# }

# def add(x,y):
#     print(x+y)
#
# add(**params)
#--------------------装饰器
# import logging
# def foo():
#     print('i am foo')
#     logging.info("foo is running")
#     print(logging.info)
#
# foo()


#------------------
# import logging
# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     print(func.__name__)
#     func()
#
# def bar():
#     print('i am bar')
#
# use_logging(bar)


#-----------------------简单装饰器
# import logging
# def use_logging(func):#装饰器
#
#     def wrapper(*args,**kwargs):
#         logging.warn("%s is running" % func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# def bar():
#     print('i am bar')
#
# bar = use_logging(bar)
# bar()

#--------------
# import logging
# def use_logging(func):
#     def wrapper(*args,**kwargs):
#         logging.warn("%s is running" % func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @use_logging
# def foo():
#     print('i am foo')
#
# @use_logging
# def bar():
#     print('i am bar')
#
# bar()
# foo()


#---------------带参数的函数装饰器，这边还带认真的思考？
# import logging
# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             return func(*args)
#         return wrapper
#     return decorator
#
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
#
# foo()

#------------------类装饰器
# class Foo(object):
#
#     def __init__(self,func):
#         self._func = func#初始化
#
#     def __call__(self):
#         print('class decorator runing')
#         self._func()
#         print('class decorator ending')
#
# @Foo
# def bar():
#     print('bar')
#
# bar()

#----------------函数作为返回值返回

#z直接返回结算结果
# def calc_sum(*args):
#
#     ax=0
#     for n in args:
#         ax=ax+n
#
#     return ax
# f=calc_sum(1,2,3)
# print(f)

#解决不立即求和，有需要的时候在计算，方式：将函数作为返回值返回
# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax=n+ax
#         return ax
#     return sum
#
# f = lazy_sum(1,2,3)
# print(f)
# print(f())#调用

#--------闭包中不能引用任何环境变量，或者后续会发生的变量，方法：在创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
# def count():
#     fs=[]
#     for i in range(1,4):
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         fs.append(f(i))
#     return fs
#
# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())

#---------------------
# def abc1():
#     def abc():
#         print("abc")
#     return abc
#
# abc1()()
#----------------
# def add(m):
#     def temp(n):
#         print(m)
#         print(n)
#         return m+n
#     # print(temp)
#     # print(m)
#     return temp
# print(add(3)(1))


#-------------------------
import os
os.chdir('C:\\Users\\Administrator\\Desktop')
print(os.path)

# if __name__=='__main__':
#     import string
#     with open('test1.txt',encoding='utf8') as f:
#         a=f.read()
#
#     with open('test2.txt',encoding='utf8') as f:
#         b=f.read()
#
#     with open('texts3.txt','w',encoding='utf8') as f:
#         l=list(a+b)
#         l.sort()
#         # print(l)
#         s=''#定义s为空字符串
#         s=s.join(l).strip()#用于将序列的元素已指定的字符连接生成一个新的字符串
#         print(s)
#         f.write(s)
#
#
#------------------------方式2
# def file_open(filename):
#     with open(filename,'r',encoding='utf8') as f:
#         return f.read()
#

#
# a=file_open('test1.txt')
#
# b=file_open('test2.txt')
# s=list("".join((a)+(b)))
# print(s)
# s.sort()
# l="".join(s)
# t=open('text3.txt','w',encoding='utf8')
# t.write(l)
# t.close()

#---------------------方式3
# with open ('test1.txt',encoding='utf8') as f1,open('test2.txt',encoding='utf8') as f2,open('test4.txt','w',encoding='utf8') as f3:
#     a=f1.read()
#     b=f2.read()
#     c=list(a+b)
#     c.sort()
#     d=''
#     d=d.join(c)
#     f3.write(d)


#----------------------



















