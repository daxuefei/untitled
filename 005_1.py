import os
os.chdir('D:\songqin\资料')

# file=open("0005_1.txt","r")
# print(file.readline())
# file.close()


def putInfoToDict(filrName):
    retDict={}
    with open(filrName) as f:
        line=f.read().splitlines()

        for line in line:
            line = line.replace('(', '').replace(')', '').replace(';', '').strip()
            print(line)

            parts=line.split(',')
            ciTime=parts[0].strip().replace("'",'')
            print(ciTime)
            lessonid=int(parts[1].strip())

            userid=int(parts[2].strip())

            toAdd={'lessonid':lessonid,'checkintime':ciTime}
            if userid not in retDict:
                retDict[userid]=[]
            retDict[userid].append(toAdd)

    return retDict
# ret=putInfoTodict('0005_1.txt')
ret = putInfoToDict('0005_1.txt')

import pprint
pprint.pprint(ret)
