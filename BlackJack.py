import random
print('Welcome to BlackJack')
name=input('Enter your Name ')
name=name.capitalize()
chips=20
print('You have',chips,'chips')
cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
while True:
    count=score=dealsc=0
    plmo=[]
    dlmo=[]
    bet=input('How many chips do you want to bet?  ')
    bet=bet.capitalize()
    if bet=='All':
        bet=chips
    elif bet=='Half':
        bet=int(chips//2)        
    else:
        bet=int(bet)
    if bet>chips:
        print("You can't bet more than what you have")
        continue
    elif bet<=0:
        print('You need to bet some chips ')
        continue
    while True:
        play=random.choice(cards)
        plmo.append(play)
        print('Card:',play)
        if play=='A':
            if score+11<=21:
                score+=11
            else:
                score+=1
        elif play=='J' or play=='Q' or play=='K':
            score+=10
        else:
            score+=play
        print('Current Score:',score)
        if score>21:
            print('You went over 21')
            break
        else:
            pass
        if score==21:
            break
        ch=int(input('''Choose one:
            1.Hit
            2.Stand
            '''))
        if ch==1:
            continue
        else:
            break
    print('Your Score',score)
    print('Your cards:',end=' ')
    print(plmo)
    while dealsc<=15:
        play=random.choice(cards)
        dlmo.append(play)
        if play=='A':
            if dealsc+11<=21:
                dealsc+=11
            else:
                dealsc+=1
        elif play=='J' or play=='Q' or play=='K':
            dealsc+=10
        else:
            dealsc+=play
    print('Dealer score:',dealsc)
    print("Dealer's cards:",end=' ')
    print(dlmo)
    if dealsc>score and dealsc<=21:
        print('The Dealer won')
        chips-=bet
    elif dealsc>21 and score>21:
        print('Nobody Won')
    elif score>dealsc and score<=21:
        print('You Win')
        chips+=bet
    elif score>21:
        print('The Dealer won')
        chips-=bet
    elif dealsc>21:
        print('You Win')
        chips+=bet
    elif dealsc==score:
        print('You Tie')
    print('Chips left:',chips)
    if chips==0:
        break
    chc=int(input('''Do you wish to play again?
            1. Yes
            2. No
            '''))
    if chc==1:
        continue
    else:
        break