






password_list=['#####','12345']

def account_login():
    times = 3
    while times >0:
        password = input('Enter your password:')
        password_correct=password==password_list[-1]
        password_reset=password==password_list[0]

        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password=input('Enter a new password:')
            password_list.append(new_password)
            print('Your password has change successful!')
            account_login()
        else:
            print('Wrong password or invaild input!')
            times=times-1
            print(times,'times left')

    else:
        print('Your password has tried more than 3 times,you can not login now!')

account_login()