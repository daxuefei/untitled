# print('****in test_calc begin****')
# import calc
# calc.calc_s(4)
# import calc
# print(calc.var1)
# print(type(calc))
# print(type(calc.calc_s))
#
#
# print('*****in test_calc end***')


# 读取文件内容
# import os
# import pprint

# os.chdir('C:\\Users\\Administrator\\Desktop')
# with open('test.txt','r')as f:
#     dir = {}
#     line = f.read().split(',')
#     # print(line)
#     for line in line:
#         name,age=line.split(':')
#         # print(type(name))
#         name = name.strip('')#直接在上面一句写strip是不对的，因为字符串不能改变，只能重新赋值
#         age = age.strip('')
#         if age in dir:
#             dir[age].append(name)
#         else:
#             dir[age] = [name]
#     print(dir)
# os.chdir()




#*********************************************找出文本中年龄段最多的是哪个年龄段**************************************
import os
os.chdir('C:\\Users\\Administrator\\Desktop')
dir={}
# line=open('test.txt').read().split(',')
def getFile(filePath):
    fh=open(filePath)
    fc=fh.read()
    fh.close()
    return fc
line=getFile('test.txt')
line=line.split(',')
c=0
for line in line:
    c+=1
    name,age=line.split(':')
    name=name.strip('')
    age=age.strip('')
    # print(type(age))
    if age in dir:
        dir[age].append(name)
    else:
        dir[age] = [name]
# print(dir)

# 计算字典中各个年龄段人的数量
curMax=0
maxCountAge=None
for age,name in dir.items():
    # print('{}岁的人数是{}人'.format(age,len(name)))
    count = len(name)
    if count >= curMax:
        curMax = count
        maxCountAge = age
print('人数最多的年龄是%s'% maxCountAge)

#************************************************ending ********************************************************








