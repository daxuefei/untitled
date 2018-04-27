#创建10个文本
def text_creat():
   desktop_path='C:/Users/Administrator/Desktop/'


   for name in range(1,11):
        with open(desktop_path+str(name)+'.txt','w') as text:#这里使用with语句，不管在处理文件过程中是否发生异常，都能保证with语句执行完毕后已关闭了打开的文件句柄
            text.write(str(name))
            text.close()
            print('Done')

text_creat()


#练习2
def principal(amount,rate,time):
    print('prinicipal amount:{}'.format(amount))
    for t in range(1,time+1):
        amount=amount*(1+rate)
        print("year{}:${}".format(t,amount))


principal(100,0.05,8)



#打印1-100内的偶数
def even_print():
    for i in range(1,101):
        if i%2==0:
            print(i)
even_print()


#random
import random
point1 = random.randrange(1,7)
print(point1)
