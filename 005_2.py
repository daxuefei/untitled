import os
os.chdir('D:\songqin\资料')

def putInfoToDict(fileName):
    dic={}
    with open('0005_1.txt','r') as f:
        line=f.read().splitlines()
        print(line)

        for line in line:
            line=line.replace('(','').replace(')','').strip()


            parts=line.split(',')
            ciTime=parts[0].strip()
            lessonid=parts[1].strip()
            userid=parts[2].strip()
            # print(parts,ciTime,lessonid,userid)

            toAdd={'userid':userid,'checkintime':ciTime}
            if lessonid not in dic:
                dic[lessonid]=[]
            dic[lessonid].append(toAdd)

            # toAdd = {'lessonid': lessonid, 'checkintime': ciTime}
            # if userid not in dic:
            #     dic[userid] = []
            # dic[userid].append(toAdd)

    return dic

ret=putInfoToDict('0005_1.txt')

import pprint
pprint.pprint(ret)




