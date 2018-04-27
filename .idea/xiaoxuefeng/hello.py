# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello,%s' % name)


def set_score(score):
    if 0 <= score <= 100:
        self.__score = score
    else:
        print('bad score')

set_score(102)