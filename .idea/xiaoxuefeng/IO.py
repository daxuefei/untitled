#-------------------------------------StringIO 在内存中读写str
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
#
# print(f.getvalue())


#------------------------读取StringIO
# from io import StringIO
# f=StringIO('Hello!\nHI\nGoodbey\n')
# while True:
#     s = f.readline()
#     if s== ' ':
#         break
#     print(s.strip())


#------------------------------序列化
#python转化为JSON
# import json
# d = dict(nmae='Bob',age=20,score=88)
# print(json.dumps(d))
#


#dict对象直接序列化为JSON，不过，很多的时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
# import json
#
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score =score
#
# s = Student('Bob',20,88)
# print(json.dumps(s))



#-----------
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s=Student()
s.birth=2010
# s.age = 2019
print(s.age)












