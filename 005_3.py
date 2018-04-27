# import os
# import pprint
#
# os.chdir('D:\songqin\资料')
#
#
# def putInfoToDict(fileName):
#     dic={}
#     with open('0005_1.txt') as f:
#         line = f.read().splitlines()
#         print(line)
#
#         for line in line:
#             line = line.replace('(', '').replace(')', '').strip()#把列表变成字符串
#             print(type(line))
#
#             parts = line.split(',')
#             ciTime = parts[0].strip()
#             lessonid=parts[1].strip()
#             userid=parts[2].strip()
#
#             toAdd={'checkintime':ciTime,'userid':userid}
#             if lessonid not in dic:
#                 dic[lessonid]=[]
#             dic[lessonid].append(toAdd)
#     return dic
#
#             # print(ciTime,lessonid,userid)
#
#
#
#
# ret=putInfoToDict('0005_1.txt')
# pprint.pprint(ret)



#作业5
# def putINfoToDict(fileName):
#     newdir = {}
#     with open(fileName,'r') as f1:
#         files=f1.read().splitlines()
#         # file=file.split(',')
#         for one in files:
#             one=one.replace("('" , "").replace("',",",").replace(",",",").replace("),",";").strip('')
#             st_id=one.split(',')[-1].strip(';')
#             le_id=one.split(',')[1]
#             checktime=one.split(',')[0]
#             ToAdd = {'lessonid': le_id,'checkintime': checktime}
#             # if st_id not in newdir:
#             #     newdir[st_id] = []
#             # newdir[st_id].append(ToAdd)
#             if st_id in newdir:
#                 newdir[st_id].append(ToAdd)
#             else:
#                 newdir[st_id]=[]
#                 newdir[st_id].append(ToAdd)
#
#     return newdir
#
#
#
# ret=putINfoToDict('0005_1.txt')
# import pprint
# pprint.pprint(ret)



#zuoye6
#1
# from phone.apple import iphone6,iphone7
# from phone.samsung.note import galaxy_note8
# from phone.samsung.s import galaxy_s7
#2
# import phone.apple.iphone6
# import phone.apple.iphone7
# import phone.samsung.note.galaxy_note8
# import phone.samsung.s.galaxy_s7

# phone.apple.iphone6.askPrice()
# phone.apple.iphone7.askPrice()
# phone.samsung.note.galaxy_note8.askPrice()
# phone.samsung.s.galaxy_s7.askPrice()

#3
# from phone.apple.iphone6 import askPrice as price1
# from phone.apple.iphone7 import askPrice  as price2
# price1()
# price2()

# #在butongmmulu
# from ceshi.phone.apple import iphone7,iphone6
# from ceshi.phone.samsung.note import galaxy_note8
# from ceshi.phone.samsung.s import galaxy_s7
# iphone6.askPrice()


# def money(n):
#     value=24.95*0.6 + 3 + 0.75*(n-1)
#     print(value)
#
# money(60)

# import math
# ratio = signal_power / noise_power
# decibels =10* math.log10(ratio)
# radians =0.7
# height=math.sin(radians)


# def print_lyrics():
#     print("I'm a lumberjack,and I'm okay")
#     print("I sleep all night and I work all day")
#
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# repeat_lyrics()

import math
# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
#
# print_twice(math.cos(math.pi))