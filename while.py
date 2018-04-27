#练习1
#while 1<3:
    #print('1 is smaller than 3')
   # break

#练习2
#count =0
#while True:
    #print('Repeat this line!')
    #count =count + 1
    #if count == 5:
#        break



#练习3 输入密码错误3此就禁止输入
password_list=['#####','12345']
times=3
def account_login():
    password = input('password:')
    paasword_correct=password==password_list[-1]
   # password_correct= password == password_list[-1]
    password_reset= password == password_list[0]
if password_correct:
    print('login successful!')
elif password_reset:
    new_password = input('Enter a new password:')
    password_list.append(new_password)
    print('Your password has changes successful!')
    account_login()
else:
    while times>0:
        print('Wrong password or invalid input!')
        times = times - 1
        if times <= 0:
            print('Your password is try 3 times,you can not login')

account_login()

