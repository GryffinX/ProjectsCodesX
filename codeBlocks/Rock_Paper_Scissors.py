import random
x=['Rock','Paper','Scissors']
t=w=l=0
while True:
    oppmove=input('''Choose move:
    Rock
    Paper
    Scissors
    ''')
    n=random.choice(x)
    oppmove=oppmove.capitalize()
    if oppmove=='Rock':
        if oppmove==n:
            print('Tie')
            t+=1
        elif n=='Paper':
            print('You Lose, The computer played',n)
            l+=1
        else:
            print('You Win')
            w+=1
    elif oppmove=='Paper':
        if oppmove==n:
            print('Tie')
            t+=1
        elif n=='Scissors':
            print('You Lose, The computer played',n)
            l+=1
        else:
            print('You Win')
            w+=1
    elif oppmove=='Scissors':
        if oppmove==n:
            print('Tie')
            t+=1
        elif n=='Rock':
            print('You Lose, The computer played',n)
            l+=1
        else:
            print('You Win')
            w+=1
    else:
        print('Are you dumb? CHOOSE FROM GIVEN OPTIONS')
        continue
    ch=int(input('''Do you want to play again?
            1. Yes
            2. No
            '''))
    if ch==1:
        continue
    else:
        print('Wins:',w,'Losses:',l,'Ties:',t)
        print('Thanks For Playing')
        break