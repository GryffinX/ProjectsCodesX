import mysql.connector as mycon
import random
def roulette():
    print('Welcome to the Roulette')
    print('You start with',chips,'chips')
    chips=10
    while True:
        bet=int(input('How many chips would you like to bet?  '))
        if bet>chips:
            print('You cannot bet more than you have')
            continue
        elif bet<0:
            print('You have to bet atleast 1 chip')
            continue
        ch=int(input('Choose a number between 1 and 10   '))
        while True:
            chc=int(input('''Choose a color:
                        1. Green
                        2. Red
                        3. Black
                        '''))
            if chc==1 or chc==2 or chc==3:
                break
            else:
                print('Please choose a valid option')
        if chc==1:
            usrco='Green'
        elif chc==2:
            usrco='Red'
        else:
            usrco='Black'
        n=random.randint(1,10)
        if n==0:
            nco='Green'
        elif n%2==0:
            nco="Red"
        else:
            nco='Black'
        if ch==n:
            print('You Won')
            chips=bet*2+chips
            print('Chips:',chips)
        else:
            if nco==usrco:
                print("You guessed wrong but your colour matched the system's")
                print('Chips:',chips)
            else:
                print('You Lost')
                chips=chips-bet
                print('Chips:',chips)
                print('The outcome:')
                print('Colour-',nco)
                print('Number-',n)
        if chips==0:
            print("Game Over")
            break
        cont=int(input('''Would you like to play again?:
                1.Yes
                2.No
                '''))
        if cont==1:
            continue
        else:
            break
    print('You ended up with',chips,'chips')
    print('Thanks for playing Roulette')
def blackjack():
    print('Welcome to BlackJack')
    chips=0
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
    print('You ended with',chips,'chips')
    print('Thanks for playing BlackJack')
con=mycon.connect(host='localhost',user='root',passwd='programming',database='casino')
if con.is_connected:
    print('yes')
    