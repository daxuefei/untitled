#----练习1
# class CocaCola:
#     formula = ['caffeine','sugar','water','soda']#在类里面赋值的变量就是类的变量，类的变量成为类的属性
#
# coke_for_me = CocaCola()#类的实例化
# coke_for_you = CocaCola()
#
# print(CocaCola)
# print(coke_for_me)
# print(coke_for_you)
# print(CocaCola.formula)#在类的名字后面输入,是类属性的引用
# print(coke_for_you.formula)
# print(coke_for_me.formula)
#
# for element in coke_for_me.formula:
#     print(element)
#

# 练习2
# class CocaCola:
#     formula = ['caffeine','sugar','water','soda']
#
# coke_for_China = CocaCola()
# coke_for_China.local_logo ='可口可乐'#创建实例属性
#
# print(coke_for_China.local_logo)#打印实例属性引用结果

#练习3
# class CocaCola:
#     formula = ['caffeine','sugar','water','soda']
#     def drink(self,how_much):
#
#         if how_much =='a sip':
#             print('Cool')
#         elif how_much == 'whole bottle':
#             print('Headance!')
#
# ice_coke =CocaCola()
# ice_coke.drink('a sip')


#练习4
#class CocaCola():
# class CocaCola():
#
#     formula = ['caffeine','sugar','water','soda']
#     def _init_(self):
#         self.local_logo = '可口可乐'
#
#     def drink(self):
#         print('Energy!')
#
# coke=CocaCola()
# print(coke.local_logo)

#删除.pyc文件
# import os
# path = 'project-path'
# for prefix, dirs, files in os.walk(path):
#     for name in files:
#         if name.endswith('.pyc'):
#             filename = os.path.join(prefix, name)
#             os.remove(filename)

# 练习6
# obj1 = 1
# obj2 = 'string'
# obj3 = []
# obj4 = {}
#
# print(type(obj1),type(obj2),type(obj3),type(obj4))

# #练习7
# from bs4 import Beautifulsoup
# soup = BeautifulSoup
# print(type(soup))


# 练习8


