dir={'20': ['William'], '15': ['Jack', 'Tom', 'Jason'], '18': ['Rachel', 'Patrick', 'Alvin', 'Mike']}
curMax=0
maxCountAge=None
for age,name in dir.items():
    count = len(name)
    if count >= curMax:
        curMax = count
        maxCountAge = age
print('人数最多的年龄是%s'% maxCountAge)