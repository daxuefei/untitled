def number1():
    number=input('Enter Your number:')
    your_number=number[0:3]
    number_len=len(number)
    if number_len = 11:
        number_list()
    else:
        print('Invalid length,your number should be in 11 digits')

number1()


def number_list():
    CN_mobile=[134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,]
    CN_union=[130,131,132,155,156,185,186,145,176]
    CN_telecon=[133,153,180,181,189,177]
    if your_number in CN_MObile:
        print('Operator:China Mobile')
    elif your_number in CN_union：
        print('Operator:China Union')
    elif you_number in CN_telecom:
        print('Operator:China Telecom')
    else:
        print('No such a operator')
