import mysql.connector as mycon
import random
from time import sleep
def roulette():
    global chips
    print('Welcome to the Roulette')
    while True:
        print('''                                                                   --RULES--
            --> You will choose a number between 0 to 36. Numbers Even numbers have the colour Red. Numbers Odd have the colour Black. 0 has the colour Green
            --> If you guess the number correctly then you win 10 times the amount you bet. If you guess and roll 0 you win 100 times
            --> If you guess wrong but your colour matches the system's colour, you lose half your bet
            --> If you guess wrong and your colour doesn't match the system's colour, you lose the amount you bet ''')
        while True:
            dch=input('''Do you want to play?
                        1. Yes
                        2. No
                        ''')
            if dch=='1':
                g=1
                break
            elif dch=='2':
                g=2
                break
            else:
                print('Invalid Choice')
                continue
        if g==1:
            pass
        else:
            print('Exiting...')
            sleep(3)   
            break     
        while True:
            bet=int(input('How many chips do you want to bet: '))
            if bet>chips:
                print('You cannot bet more than you have')
                continue
            elif bet<1:
                print('You have to bet atleast 1 chip')
                continue
            else:
                break
        while True:
            ch=int(input('Choose a number between 0 and 36:  '))
            if (ch>=0)and(ch<=36):
                break
            else:
                print('The number must be between 0 and 36')
                continue
        if ch>0:
            if ch%2==0:
                usrco='Red'
            else:
                usrco='Black'
        else:
            usrco='Green'
        n=random.randint(0,36)
        if n==0:
            nco='Green'
        elif n%2==0:
            nco="Red"
        else:
            nco='Black'
        for j in range(3):
            for i in range(1,4):
                print('  ROLLING'+('.'*i),'    ', end='\r')
                sleep(0.3)
            continue
        print('')
        for i in range(30):
            print('    ',random.randint(0,36), end='\r')
            sleep(0.1)
        print('         ')
        print('    ',n,'\n')
        if ch==n:
            if ch!=0:
                print('You won',bet*10,'chips')
                chips+=(bet*10)
                print('Balance:',chips)
            else:
                print('You won',bet*100,'chips')
                chips+=(bet*100)
                print('Balance:',chips)
        else:
            if nco==usrco:
                print("You guessed wrong but your colour matched the system's")
                if bet>1:
                    chips=chips-(bet//2)
                else:
                    chips-=bet
                print('Balance:',chips)
            else:
                print('You Lost')
                chips-=bet
                print('Balance:',chips)
        update()
        if chips==0:
            print("You Bankrupted, Game Over!")
            break
        while True:
            cont=input('''Would you like to play again?
                            1.Yes
                            2.No
                            ''')
            if cont=='1':
                mcont=1
                break
            elif cont=='2':
                mcont=2
                break
            else:
                print('Please choose a valid option')
        if mcont==1:
            continue
        else:
            print('You ended up with',chips,'chips')
            print('Thanks for playing Roulette')
            print('Exiting game...')
            sleep(3)
            break
def blackjack():
    global chips 
    cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    print('Welcome to BlackJack')
    while True:
        print('''                                           --RULES--
            --> You and the Dealer will be dealt random cards
            --> Your goal is to reach a score of 21
            --> You can choose to hit to get another card or stand to stop at your current score
            --> Dealer will choose to hit if their score is below or equal to 15
            --> Player with score more than 21 will automatically lose
            --> When both players stop, the player with score closest to 21 will win
            --> Cards 2-10 hold their face value. J,Q,K have a score of 10. A will act as 1 if your current score is more than or equal to 11 and will act as 11 if it is below 11
            --> You win or lose the amount you bet according to the result. Ties result in no loss and no gain''')
        while True:
            och=input('''Do you want to play?
                        1. Yes
                        2. No
                        ''')
            if och=='1':
                e=1 
                break
            elif och=='2':
                e=2
                break
            else:
                print('Invalid Choice')
                continue
        if e==1:
            pass
        else:
            print('Exiting...')
            sleep(3)
            break
        count=score=dealsc=0
        plmo=[]
        dlmo=[]
        while True:
            bet=int(input('How many chips do you want to bet:  '))
            if bet>chips:
                print("You can't bet more than what you have")
                continue
            elif bet<=0:
                print('You need to bet atleast 1 chip')
                continue
            else:
                break
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
            while True:
                ch=input('''Choose one:
                                1.Hit
                                2.Stand
                                ''')
                if ch=='1':
                    cc=1
                    break
                elif ch=='2':
                    cc=2
                    break
                else:
                    print('Invalid Option')
            if cc==1:
                continue
            else:
                break
        print('Your Score:',score)
        print('Your Cards:',end=' ')
        for i in range(len(plmo)-1):
            print(plmo[i],end=',')
        print(plmo[-1])
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
        print("Dealer's Score:",dealsc)
        print("Dealer's Cards:",end=' ')
        for i in range(len(dlmo)-1):
            print(dlmo[i],end=',')
        print(dlmo[-1])
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
        print('Balance:',chips)
        update()
        if chips==0:
            print('You Bankrupted, Game Over!')
            break
        while True:
            chc=input('''Would you like to play again?
                            1. Yes
                            2. No
                            ''')
            if chc=='1':
                mchc=1
                break
            elif chc=='2':
                mchc=2
                break
            else:
                print('Please choose a valid option')
        if mchc==1:
            continue
        else:
            print('You ended with',chips,'chips')
            print('Thanks for playing BlackJack')
            print('Exiting game...')
            sleep(3)
            break
def slots():
    global chips
    print('Welcome to Slots')
    while True:
        a=0
        print('''PAYOUTS:
            PATTERN                        PAY
        7️⃣    7️⃣    7️⃣                    2500 Chips 
        🔔   🔔   🔔                    500 Chips
        💀   💀   💀                    200 Chips
        🍋   🍋   🍋                    100 Chips
        🍒   🍒   🍒                     75 Chips
         X    X   ___                     3 Chips''' ) 
        print('Each Spin costs 1 chip')
        s=['7️⃣','7️⃣','7️⃣']
        be=['🔔','🔔','🔔']
        b=['💀','💀','💀']
        l=['🍋','🍋','🍋']
        c=['🍒','🍒','🍒']
        s=[['7️⃣','7️⃣'],['🔔','🔔'],['💀','💀'],['🍋','🍋'],['🍒','🍒']]
        pat=['7️⃣','🔔','🔔','💀','💀','💀','🍋','🍋','🍋','🍋','🍒','🍒','🍒','🍒','🍒']
        whl1=whl2=whl3=0
        whl1=random.choice(pat)
        whl2=random.choice(pat)
        whl3=random.choice(pat)
        play=[]
        while True:
            chp=input('''Would you like to spin?
                        1. Yes
                        2. No
                        ''')
            if chp=='1':
                pchp=1
                break
            elif chp=='2':
                pchp=2
                break
            else:
                print('Invalid Choice')
        if pchp==1:
            chips-=1
            pass
        else:
            print('Exiting...')
            sleep(3)
            break
        while a<10:
            x=random.choice(pat)
            y=random.choice(pat)
            z=random.choice(pat)
            print('   |',x,'~',y,'~',z,'|             ',end='\r')
            sleep(0.2)
            a+=1
        print('   |',whl1,'~',y,'~',z,'|    ',end='\r')
        while a<24:
            y=random.choice(pat)
            z=random.choice(pat)
            print('   |',whl1,'~',y,'~',z,'|       ',end='\r')
            sleep(0.2)
            a+=1
        print('   |',whl1,'~',whl2,'~',z,'|    ',end='\r')
        while a<43:
            z=random.choice(pat)
            print('   |',whl1,'~',whl2,'~',z,'|      ',end='\r')
            sleep(0.2)
            a+=1
        print('   |',whl1,'~',whl2,'~',whl3,'|     ',end='\n')
        play.append([whl1,whl2,whl3])
        p1=[play[0][0],play[0][1]]
        p2=[play[0][1],play[0][2]]
        p3=[play[0][0],play[0][2]]
        if play[0]==s:
            print('JACKPOT!')
            print('You won 2500 Chips')
            chips+=2501
        elif play[0]==be:
            print('Congratulations! You got a Bell pattern')
            print('You won 500 Chips ')
            chips+=501
        elif play[0]==b:
            print('Congratulations! You got a Skull pattern')
            print('You won 200 Chips')
            chips+=201
        elif play[0]==l:
            print('Congratulations! You got a Lemon pattern')
            print('You won 100 Chips')
            chips+=101
        elif play[0]==c:
            print('Congratulations! You got a Cherry pattern')
            print('You won 75 Chips')
            chips+=76
        elif (p1 in s) or (p2 in s) or (p3 in s):
            print('You rolled two of the same pattern')
            print('You won 3 Chips')
            chips+=4
        else:
            print("You didn't win anything")
            print('Balance:',chips)
        if chips==0:
            print('You Bankrupted, Game Over!')
            break
        while True:
            pch=input('''Would you like to play again?
                            1. Yes
                            2. No
                            ''')
            if pch=='1':
                ppch=1
                break
            elif pch=='2':
                print('You ended with',chips,'chips')
                print('Thank you for playing Slots!')
                print('Exiting...')
                sleep(3)
                ppch=2
                break
            else:
                print('Invalid Choice')
                continue
        if ppch==1:
            continue
        else:
            break
def dtoss():
    global chips
    v=0
    print('Welcome to Die Toss')
    mult=tmult=1
    while True:
        print('''                                                  --RULES--
            --> If you roll the guessed number, you gain a winning multiplier of 1x on your existing multiplier
            --> As you win, your bet multiplier also increases by 0.5x
            --> You start with a multiplier of 1x''')
        while True:
            ich=input('''Do you want to play?
                        1. Yes
                        2. No
                        ''')
            if ich=='1':
                v=1
                break
            elif ich=='2':
                break
            else:
                print('Invalid Choice')
                continue
        if v==1:
            pass
        else:
            print('Exiting...')
            sleep(3)
            break
        while True:
            tch=int(input('How many chips do you want to bet: '))
            if (tch>chips) or (tch<1):
                print('Invalid Choice, Please choose chips according to you balance')
                continue
            else:
                break
        while True:
            nguess=int(input('Guess the number between 1-6: '))
            if (nguess<1) or (nguess>6):
                print("Invalid Number, Please Guess Between 1 and 6")
                continue
            else:
                break
        outcome=random.randint(1,6)
        if nguess==outcome:
            print('You guessed correct')
            print('You won',int(tch*mult),'chips')
            chips+=int(tch*mult)
            mult+=1
            tmult+=0.5
            print('Multiplier --->',float(mult))
            print('Bet Multiplier --->',tmult)
        else:
            print('You guessed wrong')
            print('Outcome:',outcome)
            print('You lost',int(tch*tmult),'chips')
            chips-=int(tch*tmult)
            print('Balance:',int(chips))
            tmult=mult=1
            print('Multiplier --->',mult)
            print('Bet Multiplier --->',tmult)
        print('Balance:',chips)
        update()
        if chips==0:
            print('You Bankrupted, Game Over!')
            break
        while True:
            ach=input('''Would you like to play again?
                        1. Yes
                        2. No
                        ''')
            if ach=='1':
                ech=1
                break
            elif ach=='2':
                ech=2
                print('You ended with',int(chips),'chips')
                print('Thank you for playing Die-Toss')
                print('Exiting...')
                sleep(3)
                break
            else:
                print('Invalid Choice')
                continue
        if ech==1:
            continue
        else:
            break
def horse():
    global chips
    z=0
    while True:
        print('''                     --RULES--
        --> You have 5 Horses to choose from
        --> Horses will race to 100m
        --> If your horse wins, you win 2 times the amount you betted
        --> If your horse ties, you win or lose nothing
        --> If your horses loses, you lose the amount you betted
        --> Happy Racing!''')
        while True:
            ych=input('''Do you want to play?
                        1. Yes
                        2. No
                        ''')
            if ych=='1':
                break
            elif ych=='2':
                z=2
                break
            else:
                print('Invalid Choice')
                continue
        if z==2:
            print('Exiting...')
            sleep(3)
            break
        while True:
            print('              HORSES:')
            print('1. Ghost')
            print('2. Grace')
            print('3. Max ')
            print('4. Joey')
            print('5. Jamal')
            hch=input('Choose a horse: ')
            if hch=='1':
                usrho='Ghost'
                break
            elif hch=='2':
                usrho='Grace'
                break
            elif hch=='3':
                usrho='Max'
                break
            elif hch=='4':
                usrho='Joey'
                break
            elif hch=='5':
                usrho='Jamal'
                break
            else:
                print('Invalid Choice')
                continue
        h=['Ghost','Grace','Max','Joey','Jamal']
        while True:
            hbet=int(input('How many chips do you want to bet: '))
            if (hbet<1) or (hbet>chips):
                print('Invalid Choice, Choose again')
                continue
            else:
                break                                                
        print('RACE BEGINS!')
        sleep(1.5)
        td1=td2=td3=td4=td5=100
        print('DISTANCE LEFT: 100 METERS')
        print('\n')
        while True:
            hb=0
            d1=random.randint(0,10)
            td1-=d1
            d2=random.randint(0,10)
            td2-=d2
            d3=random.randint(0,10)
            td3-=d3
            d4=random.randint(0,10)
            td4-=d4
            d5=random.randint(0,10)
            td5-=d5
            hd=[d1,d2,d3,d4,d5]
            dh=[td1,td2,td3,td4,td5]
            for i in range(len(dh)):
                if dh[i]<=0:
                    print('A horse has reached the finish line.')
                    hb=1
                    break
            if hb==1:
                break
            for i in range(len(h)):
                print(h[i],'moved',hd[i],'meters, distance left:',dh[i],'meters')
            print('\n')
            sleep(3)
        t=[]
        wd=0
        for a in dh:
            if a<wd:
                wd=a
        t.append(wd)
        u=dh.index(wd)
        dh.remove(wd)
        for i in dh:
            if i==wd:
                t.append(i)
        dh.insert(u,wd)
        win=[]
        for i in t:
            wd=dh.index(i)
            dh.remove(dh[wd])
            hw=h[wd]
            h.remove(hw)
            win.append(hw)
        if len(win)>1:
            print('We have a tie between: ',end='')
            for i in win:
                print(i,end=' ')
            print('')
            if usrho in win:
                print('Your horse tied, you didnt win or lose anything. Chips:',chips)
            else:
                print('Your horse was not among the winners. You lost the amount you bet. Chips:',chips-hbet)
                chips-=hbet
        elif len(win)==1:
            print(win[0],'wins!')
            if usrho==win[0]:
                    print('Your horse wins, you won',hbet*2,'chips. Chips:',chips+(hbet*2))
                    chips+=(hbet*2)
            else:
                print('Your horse didnt win. You lost',hbet,'chips. Chips:',chips-hbet)
                chips-=hbet
        print('Balance:',chips)
        update()
        if chips==0:
            print('You Bankrupted, Game Over')
            break
        while True:
            rch=input('''Would you like to play again
                        1. Yes
                        2. No
                        ''')
            if rch=='1':    
                rb=1
                break 
            elif rch=='2':
                print('Thank you for playing Horse-Racing')
                print('You ended with',chips,'chips')
                print('Exiting...')
                sleep(3)
                rb=2
                break
            else:
                print('Invalid Choice')
                continue
        if rb==1:
            continue
        else:
            break
con=mycon.connect(host='localhost',user='root',passwd='programming',database='casinoprac')                          # DB- Casinoprac, TABLE- wallet
cur=con.cursor()
def update():
    global chips
    global idchk
    upq='update wallet set chips=%s where id=%s;'
    upval=(chips,idchk)
    cur.execute(upq,upval)
    con.commit()
def newid():
    global chips
    global idchk
    re=0
    while True:
        name=input('Enter your Name(max 10 characters): ')
        if len(name)>10:
            print('Name cannot have more than 10 characters')
            continue
        elif len(name)==0 or name in (' '*11):
            print('Name cannot be empty')
            continue
        for i in name:
            if not i.isalpha():
                re=1
                break
        if re==1:
            print('Name can only contain alphabets')
            re=0
            continue
        else:
            break
    while True:
        usrnm=input('Choose and enter a new Username(max 10 characters): ')
        if len(usrnm)>10:
            print('Username cannot have more than 10 characters')
            continue
        elif len(usrnm)==0 or usrnm in (' '*11):
            print('Username cannot be empty')
            continue
        for i in usrnm:
            if not i.isalnum():
                re=2
                break
        if re==2:
            print('Username can only contain letters and numbers')
            re=0
            continue
        else:
            break
    while True:
        pas=input('Choose your password(max 10 characters): ')
        if len(pas)>10:
            print('Password cannot have more than 10 characters')
            continue
        elif len(pas)==0 or pas in (' '*11):
            print('Password cannot be empty')
            continue
        for i in pas:
            if not(i.isalnum() or i=='_'):
                re=3
                break
        if re==3:
            print('Password can only contain alphabets, numbers and underscores')
            re=0
            continue
        else:
            break
    chisp=100
    det=0
    squery='insert into wallet(name,usrnm,chips,passwd,debt) values(%s,%s,%s,%s,%s)'
    val=(name,usrnm,chisp,pas,det)
    cur.execute(squery,val)
    con.commit()
    cur.execute('select id from wallet where usrnm=%s and name=%s;',(usrnm,name))
    xx=cur.fetchone()
    sleep(1)
    print('Your ID is',xx[0])
    idchk=xx[0]
    chips=100
def loan():
    global chips
    ret=0
    while True:
        while True:
            lamt=input('''Choose an amount to borrow:
                               CHIPS               AMOUNT TO BE PAID BACK
                            1. 25 Chips                    75 Chips
                            2. 50 Chips                    150 Chips
                            3. 75 Chips                    225 Chips
                            4. 100 Chips                   300 Chips
                            5. 150 Chips                   450 Chips
                            6. Custom Amount
                            7. Exit
                            ''')
            if lamt=='1':
                loan=25
                break
            elif lamt=='2':
                loan=50
                break
            elif lamt=='3':
                loan=75
                break
            elif lamt=='4':
                loan=100
                break
            elif lamt=='5':
                loan=150
                break
            elif lamt=='6':
                loan=int(input("Enter amount you want to borrow: "))
                break
            elif lamt=='7':
                ret=1
                break
            else:
                print('Invalid Option')
                continue
        if ret==1:
            break
        ndebt=loan*3
        while True:
            dpass=input('Enter your password to continue: ')
            if dpass==chkpass:
                cur.execute('update wallet set debt=debt+%s where id=%s;',(ndebt,idchk))
                chips+=loan
                update()
                print('Action successful')
                break
            else:
                print('Incorrect Password, Try Again')
                continue
        print('You have borrowed',loan,'chips and have to pay back',ndebt,'chips')
        sleep(1)
        break
def payloan():
    global chips
    ret=0
    cur.execute('select debt from wallet where id=%s',(idchk,))
    pdebt=cur.fetchone()[0]
    print('Your pending debt:',pdebt,'chips')
    while True:
        while True:
            cdebt=int(input('How many chips do you want to pay? '))
            if cdebt>pdebt:
                print('You cannot pay more than you owe')
                continue
            elif cdebt<0:
                print('Invalid Choice')
                continue
            else:
                break
        pdebt-=cdebt
        print('You paid',cdebt,'chips and pending debt is',pdebt,'chips')
        while True:
            ppass=input('Enter your password to confirm: ')
            if ppass==chkpass:
                cur.execute('update wallet set debt=%s where id=%s;',(pdebt,idchk))
                con.commit()
                chips-=cdebt
                update()
                print('Payment Successful!')
                break
            else:
                print('Incorrect Password, Try Again')
                continue
        sleep(1)
        break
print('Welcome to Casino Games!')
while True:
    ch1=input('''Are you a New User?
                    1. Yes
                    2. No
                    ''')
    if ch1=='2':
        break
    elif ch1=='1':
        newid()
        break
    else:
        print('Invalid Choice')
cur.execute('select * from wallet')
xxx=cur.fetchall()
while True:
    idchk=int(input('Enter your ID: '))
    cur.execute('select id from wallet;')
    ids=cur.fetchall()
    for i in ids:
        if idchk==i[0]:
            re=1
            break
    else:
        print("ID doesn't exist")
        print('Check entered ID or get new ID')
        continue
    if re==1:
            break

for j in xxx:
    if j[0]==idchk:
        chkpass=j[4]
while True:
    passchk=input('Enter your password to continue: ')
    if passchk==chkpass:
        print('Login Successful!')
        sleep(1)
        break
    else:
        print('Incorrect Password, Try Again')
        continue
for i in xxx:
    if i[0]==idchk:
        chips=i[3]
        user=i[2]
print('Welcome',user)
print('You have',chips,'chips')
while True:
    chb=0
    if chips==0:
        while True:
            bch=input('''Choose:
                            1. Take a loan
                            2. New ID
                            3. Exit
                            ''')
            if bch=='2':
                newid()
                chb=1
                break
            elif bch=='3':
                chb=2
                print('Exiting...')
                sleep(3)
                break
            elif bch=='1':
                chb=1
                loan()
                break
            else:
                print('Invalid Choice')
                continue
    if chb==1:
        pass
    elif chb==2:
        break
    cur.execute('select debt from wallet where id =%s;',(idchk,))
    d=cur.fetchone()
    debt=d[0]
    mch=input('''Choose a Game to play or another option:
                        1. Roulette
                        2. BlackJack
                        3. Slots
                        4. Die-Toss
                        5. Horse-Racing
                        6. Check Balance
                        7. Get New ID
                        8. Change Username
                        9. Change Name
                       10. Change Password
                       11. Loan System
                       12. Exit
                       ''')
    if mch=='1':
        roulette()
    elif mch=='2':
        blackjack()
    elif mch=='3':
        slots()
    elif mch=='4':
        dtoss()
    elif mch=='5':
        horse()
    elif mch=='6':
        cur.execute('select chips from wallet where id=%s',(idchk,))
        bal=cur.fetchone()[0]
        print('Your balance is',bal)
        sleep(1)
    elif mch=='7':
        newid()
    elif mch=='8':
        nusrnm=input('Enter new username: ')
        while True:
            cpass=input('Enter password to confirm: ')
            if cpass==chkpass:
                break
            else:
                print('Incorrect Password, Try Again')
                continue
        cur.execute('update wallet set usrnm=%s where id=%s',(nusrnm,idchk))
        sleep(1)
        print('Action Successful')
        con.commit()
    elif mch=='9':
        cname=input("Enter new Name: ")
        while True:
            cpass2=input('Enter password to confirm: ')
            if cpass2==chkpass:
                break
            else:
                print('Incorrect Password, Try Again')
                continue
        cur.execute('update wallet set name=%s where id=%s',(cname,idchk))
        con.commit()
        sleep(1)
        print('Action Successful')
    elif mch=='10':
        while True:
            while True:
                npass=input('Enter new Password: ')
                rnpass=input('Re-enter Password to confirm: ')
                if npass==chkpass:
                    print('New Password cannot be the same as Old password')
                    continue
                else:
                    break
            if rnpass==npass:
                break
            else:
                print('Passwords dont match, Try Again')
                continue
        while True:
            olpass=input('Enter old Password to confirm: ')
            if olpass==chkpass:
                chkpass=npass
                break
            else:
                print('Incorrect Password, Try Again')
                continue
        cur.execute('update wallet set passwd=%s where id=%s',(npass,idchk))
        con.commit()
        sleep(1)
        print('Action Successful')
    elif mch=='11':     
        while True:
            lch=input('''Choose an option:
                        1. Take Loan
                        2. Pay Debt
                        3. Check Debt
                        4. Exit
                        ''')
            if lch=='1':
                loan()
            elif lch=='2':
                payloan()
            elif lch=='3':
                cur.execute('select debt from wallet where id=%s',(idchk,))
                rdebt=cur.fetchone()
                print('Your pending debt is:',rdebt[0])
                sleep(1)
            elif lch=='4':
                print('Exiting...')
                sleep(1)
                break
            else:
                print('Invalid Choice')
                continue
    elif mch=='12':
        print('You ended with',chips,'chips')
        print('Exiting the program...')
        sleep(3)
        break
    else:
        print('Invalid Option')
print('Thank You for playing Casino Games!')