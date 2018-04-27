#摇3个色子
import random
def roll_dice(numbers=3,points=None):
    print('<<<<<ROLL THE DICE!>>>>>>')
    if points is None:
        points=[]
    while numbers>0:
        point =random.randrange(1,7)
        points.append(point)
        numbers=numbers-1
    return points
#求3个色子的总和，并判断是大还是小
def roll_result(total):
    isBIG=11<=total<=18
    isSMALL=3<=total<=10
    if isBIG:
        return 'BIG'
    elif isSMALL:
        return 'SMALL'
#开始游戏，让用户猜大小，并定义什么是对什么是错，输入结果
def start_game():
    bet=1000
    print('<<<<GAME START!>>>>')
    while bet>0:
        choices=['BIG','SMALL']
        your_choice=input('BIG or SMALL:')
        your_bet=input('How much you wanna bet?-')
        if your_choice in choices:
            points=roll_dice()
            total=sum(points)
            youWin=your_choice==roll_result(total)
            if youWin:
                print('The points are',points,'You win!')
                bet=bet+int(your_bet)
                print('You lost {},You have {} now'.format(your_bet,bet))
            else:
                print('The points are',points,'You lose!')
                bet=bet-int(your_bet)
                print(bet)
                print('You lost {},You have {} now'.format(your_bet, bet))
        else:
            print('Invalid Words')
            start_game()
    else:
        print('GAME OVER')
start_game()


#