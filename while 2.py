password_list=['#*#*','12345']

def account_login():
    tries=3
    while tries >0:
        password =input('Password:')

        password_reset=password == password_list[0]
        password_correct = password == password_list[-1]

        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password =input('Enter a new password:')
            password_list.append(new_password)
            print('Password hsa changed successful!')
        else:
            print('Wrong password or invaild input!')
            tries=tries -1
            print(tries,'times left')
    else:
        print('Your account has been suspended')

account_login()




long(123)