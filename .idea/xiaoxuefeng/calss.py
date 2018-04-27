#------------------------------类:class+类名，类名通常为大写开头的单词，紧接着是（object），表示该类是从哪个类继承的，通常是object
# class Student(object):
#     pass

#---------------------多重继承
# class Animal(object):
#     pass

# #大类
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# #各种动物
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Runing.........')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying..........')
#
#
# class Dog(Mammal,Runnable):
#     pass
#
# class Bat(Mammal,Flyable):
#     pass
#
#
# c=Dog()
# c.run()

#---------------------------------枚举类
#月份
# from enum import Enum
# Month = Enum('Mouth',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
#
# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)

#周
# from enum import Enum
# Weekday = Enum('Weekday',('Mon','Tue','Wen','Thu','Fir'))
#
# for name,member in Weekday.__members__.items():
#     print(name,'=>',member,',',member.value)


#
# from enum import Enum,unique
#
# @unique
# class Weekday(Enum):
#     Sum = 0
#     Mon =1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# day1 = Weekday.Mon
# print(day1)
# print(Weekday.Tue.value)
# print(day1==Weekday.Mon)

# def enum import Enum,unique
#
# @unique
# class Gender(Enum):


#------------------------------------------------使用元类
# from hello import Hello
# h=Hello()#实例化
# print(h)
# print(h.hello())
# print(type(Hello))
# print(type(h))



#--------------------------
# def fn(self,name='world'):#先定义函数
#     print('Hello,%s' % name)
#
# Hello = type('Hello',(object,),dict(hello = fn)) #创建Hello class
#
# h=Hello()
# print(h.hello)
# print(type(Hello))
# print(type(h))

#--------------------------------
# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add'] =lambda self,value:self.append(value)
#
#         return type.__new__(cls,name,bases,attrs)
#
# class MyList(list,metaclass=ListMetaclass):
#     pass
# L=MyList()
# L.add(2)
# print(L)

#---------------------------------ORM框架
# class User(Model):
#     #定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# #创建一个实例
# u = User(id=12345,name='Micheal',email='test@orm.org',password='my_pwd')
# #保存到数据库
# u.save()
#
# class Field(object):
#
#     def __init__(self,name,column_type):
#         self.name =name
#         self.column_type =column_type
#
#     def __str__(self):
#         return '<%s:%s>' %(self.__class__.__name__. self.name)

#---------------------限制访问
# class Student(object):
#
#     def __init__(self,name,score):
#         self.__name=name
#         self.__score=score
#
#     def print_score(self):
#         print('%s:%s' %(self.__name,slef.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self,score):
#         self.__score=score
#
#         # if  0<= score <= 100:
#         #     self.__score = score
#         # else:
#         #     print('bad score')
#
# bart=Student('Bart Simpson',102)
# #不能直接访问_name是因为python解释器对外把_name变量改成_Studeent__name,所以，依然可以通过_Student__name来访问__变量
# print(bart._Student__name)
# print(bart.get_name())
# print(bart.get_score())
# bart.__score= 122
# print('bart.get_score() =',bart.get_score())
# print('bart.set_score() =',bart.__name(),bart.set_score())
# print(bart._Student__set_score)


#---------------练习
# class Student(object):
#
#     def __init__(self,name,gender):
#         self.__name=name
#         self.__gender=gender
#
#     def print_gender(self):
#         print('%s:%s' %(self.__name,self.__gender))
#
#     def get_name(self):
#         return self.name
#
#     def get_gender(self):
#         return self.gender
#
#     def set_gender(self,gender):
#         if gender == 'male' or gender == 'female':
#             self.__gender = gender
#         else:
#             raise ValueError('wrong gender')
#
#
# # bart=Student('Tony','男'）
# bart=Student('Bart Simpson','hahahahha')
# print(bart._Student__name)
# print(bart._Student__gender)

#-----------------------
# class Student(object):
#
#     def __init__(self,name,gender):
#         self.__name = name
#         self.__gender = gender
#     def print_gender(self):
#         print('%s: %s' % (self.name,self.gender))
#     def get_gender(self):
#         return self.gender
#     def set_gender(self,gender):
#         L = ['男','女']
#         if gender in L:
#             self.gender = gender
#         else:
#            print('bad gender')
#
# Bart=Student('Simpson','male')
# print(Bart._Student__name)
# print(Bart._Student__gender)


#继承和多态
# class Animal(object):
#     def run(self):
#         print('Animal is runing...')
# #
# class Dog(Animal):
#     def run(self):
#         print('dog is runing....')
#
#     def eat(self):
#         print('dog is eating....')
#
# class Cat(Animal):
#     def run(self):
#         print('cat is runing....')
#
# dog=Dog()
# dog.run()
# dog.eat()
# cat=Cat()
# cat.run()

#-------多态的好处
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# run_twice(Dog())

#-----------给实例绑定一个属性
class Student(object):
    pass
# s=Student()
# s.name='Michael'
# print(s.name)
# #----------给实例绑定一个方法
# def set_age(self,age):#定义一个函数作为实例方法
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age,s)#给实例绑定一个方法
# s.set_age(25)#调用实例方法
# print(s.age)#测试结果
#
# #给一个实例绑定方法，对另一个实例不起作用，要给所有的实例绑定方法，可以给clss绑定方法
# s2 = Student()
# s2.set_age(26)
# # print(s2.age)

#----给类绑定方法
# def set_score(self,score):
#     self.score =score
#
# Student.set_score = set_score
#
# s3 = Student()
# s3.set_score(100)
# print(s3.score)

#--------------显示实例属性，至允许对Student 添加name和age属性
# class Student():
#     __slots__=('name','age')
#
# s=Student()
# s.name = 'Michael'
# s.age=26
# # s.score ='99'
# print(s.name)
# print(s.age)
#
# class GraduateStudent(Student):
#     pass
# g=GraduateStudent()
# g.score = 9999
# print(g.score)

#-------------------------@property
# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value <10 or value >100:
#             raise ValueError('score must between 0~100!')
#         self._score = value
#
# s=Student()
# s.set_score(2.4)



#----------------
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an interger!')
#         if value<0 or value >100:
#             raise ValueError('score must between 0~100!')
#         self._score =value
#
# s=Student()
# s.score=9
# print(s.score)
# s.soore=9
# print(s.score)

#-----定义只读属性，只定义getter
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
# #定义setter，定义可读写属性
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#
# #不定义setter，就只有只读属性，即age只有只读属性
#     @property
#     def age(self):
#         return 2018 - self._birth
#
# s=Student()
# s.birth = 1991
# print(s.age)

#-----------------------
# class Screen(object):
#
#     @property
#     def width(self):
#         return self.width
#     @width.setter
#     def witdth(self,value1):
#         self._witdth = value1
#         # self.witdth = value1
#
#
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value2):
#         # self.height = value2
#         self._height = value2
#
#     @property
#     def resolution(self):
#         return self._witdth*self._height
#         # return self.witdth * self.height
#
# s=Screen()
# s.witdth = 5
# s.height = 6
# print(s.resolution)


#-------------多重继承
# class Animal(object):
#     pass
# #大类
# class Mammal(Animal):
#     pass
#
# #各种动物
# class Dog(Mammal):
#     pass
#
# class Bat(Mammal):
#     pass
#
# class Parrot(Bird):
#     pass
#
# class Ostrich(Bird):
#     pass
#
# class Runnable(object):
#     def run(self):
#         print('Running....')
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
# class Dog(Mammal,Runnable):
#     pass
#
# class Bat(Mammal,Flyable):
#     pass


#------------------python多重继承
# class A(object):
#     def foo(self):
#         print('A foo')
#     def bar(self):
#         print('A bar')
#
# class B(object):
#     def foo(self):
#         print('B foo')
#     def bar(self):
#         print('B bar')
#
# class C1(A,B):
#     pass
#
# class C2(A,B):
#     def bar(self):
#         print('C2 bar')
#
# class D(C1,C2):
#     pass
#
# if __name__=='__main__':
#     print(D.__mro__)
#     d=D()
#     d.foo()
#     d.bar()

#--------------------------枚举类
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/content").childSelector(new UiSelector().className("android.view.View )).fromParent(new UiSelector().index("3"))')




























