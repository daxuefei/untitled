#-*- encoding:utf-8 -*-
# from uiautomator import Device
# d=Device('')  # 当只有一台设备连接时可不指定序列号
# print (d.info)
# # d.press(0x07, 0x02)
#d.click(70, 1400)#点击“登录”按钮
#d.click(940,963)#点击查看明文密码

#UiObject delete = new UiObject(new UiSelector().resourceId("com.xiniunet.xntalk:id/nim_message_item_text_body"))#的控件名
          #delete.longClick()#长按

# #Turn on/off screen
# d.screen.on()
# #sleep(5)
# d.screen.off()

#wake up tee device
#d.wakeup()
#sleep()
# d.sleep()


# #appium
# from appium import webdriver
# des = {}
# des['platformName'] = 'Android'
# des['platformVersion'] = '4.2'
# des['deviceName'] = 'Android Emulator'
# des['app'] = "C:\\Users\Administrator\\Desktop\\testappium\\list1.2.apk"
# webdriver.Remote('http://localhost:4723/wd/hub', '')

#onView(withId(R.id.editName))
# onView(withId(R.id.editName)).perform(click(), replaceText("..."), closeSoftKeyboard())

# def profit():
#     i = int(input('净利润:'))
#     if i <= 10:
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
#     print(j)
#
# profit()

# movies=["Holy Grail","The life of Brian","The Meaning of Life"]
# movies.insert(1,"1975")
# movies.insert(3,"1979")
# movies.insert(5,"1983")
# movies.append(["Michale","John","Eric"])
# print(movies)
# print(movies[6][2])


#打印嵌套列表
# def print_lol(the_list):
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item)
#             # print(each_item)
#         else:
#             print(each_item)
#
# print_lol(movies)






#while迭代
# count=0
# while count<len(movies):
#     print(movies[count])
#     count+=1
#for迭代
# for i in movies:
#     print(i)

# import sys
# print(sys.path)


# def t2(para):
#     para[0]=3
#
# b=[1]
# print(t2(b))


# def t2(para):
#     para=3
#
# b=[1]
# print(t2(b))

# def e1():
#     print('in e1')
#     return False
#
# e1()
# import os
# os.chdir('D:\songqin\资料')
#
# def putInfoToDict(fileName):
#     dic={}
#     with open(fileName,'r') as f:
#         line=f.read().splitlines()
#
#
#         for line in line:
            # line = line.replace('(', '').replace(')', '').replace(';', '').strip()
            # lin/




            # print(ciTime,lessonid,userid)
# ret=putInfoToDict('0005_1.txt')
#
# from pprint import pprint
# pprint(ret)
#按大小排序
# list1=[23,4,56,3,34,5,43,76,53]
# def mySort(list):
#     newList=[]
#     for one in range(len(list)):
#         newList.append(min(list))
#         list.remove(min(list))
#     return newList
#
# print(mySort(list1))

#练习2
# def sort(inList):
#     newList = []
#
#     while len(inList)>0:
#         theMin = inList[0]#记录当前循环最小元素
#         minIdx =0#记录当前元素的下标
#         idx =0 #指向当前元素下标
#         for one in inList:
#             if theMin > one:
#                 theMin = one
#                 minIdx = idx
#             idx +=1
#         inList.pop(minIdx)
#         newList.append(theMin)
#
#     return newList
# print(sort([1,3,5,7,78,64,23,21,343]))

#从文本中取出信息，分行处理后，存到另一个文本中
#方式一：

with open('./file1.txt','r') as f1,open('./file2.txt','w') as f2:
    file1=f1.read()
    for line in file1.split('\n'):
        if line.strip()=='':
            continue
        parts=line.split('\t')
        name,salary=parts[0].split(';')
        name=name.split(':')[1].strip()
        salary=int(salary.split(':')[1])
        file3='name:%5s   ;salary:%5d   ;tax:%5d   ;income:%5d ' % (name,salary,salary*0.1,salary*0.9)
        print(file3)
        fil2=f2.write(file3 +'\n')


方式二
inFileName = 'file1.txt'
outFileName = 'file2.txt'
with open(inFileName) as ifile,open(outFileName,'w') as ofile:
    beforeTax = ifile.read().splitlines()
    for one in beforeTax:
        if one.count(';') != 1:
            countinue
        namePart,salaryPart = one.split(';')
        if namePart.count(':') != 1:
            countinue
        if salaryPart.count(':') != 1:
            countinue
        name = namePart.split(':')[1].strip()
        salary = salaryPart.split(':')[1].strip()
        income = int(int(salary)*0.9)
        tax = int(int(salary)*0.1)
        outPutStr = 'name:{:10};salary:{:10};tax:{:6};income:{:6}'.format(name,salary,tax,income)
        print(outPutStr)
        ofile.write(outPutStr + '\n')
        









































