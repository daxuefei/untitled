#password_list=['****','12345']
def account_login():
    password=input('Password:')
    password_correct=password==password_list[-1]
    password_reset=password==password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password=input('Enter a new password')
        password_list.append(new_password)
        print('Your password hsa changed successfully!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
#account_login()


















#练习1
#password_list=['#####','12345']
#def account_login():
    password=input('password:')
    password_correct=password==password_list[-1]
    password_reset=password==password_list[0]
    if password_correct:
        print('login successful!')
    elif password_reset:
        new_password=input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changes successful!')
        account_login()
    else:
        print('Wrong password or invalid input!')
        account_login()
#account_login()




#练习2
#for num in range(1,11):
    #print(str(num)+'+1=',num+1)

#练习3
#songslist=['Holy Diver','Thunderstruck','Rebel']
#for song in songslist:
    if song =='Holy Diver':
        print(song,'-Dio')
    elif song =='Thunderstruck':
        print(song,'-AC/DC')
    elif song=='Rebel':
       # print(song,'-David')





#









