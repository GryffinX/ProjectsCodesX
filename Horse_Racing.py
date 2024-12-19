import random 
import time
def horse():
    chips=50
    while True:
        print('Welcome to Horse-Racing')
        print('''
            --> You have 5 Horses to choose from
            --> Horses will race to 100m
            --> If your horse wins, you win 2 times the amount you betted
            --> If your horse ties, you win or lose nothing
            --> If your horses loses, you lose the amount you betted
            --> Happy Racing!''')
        r=input('Press ENTER to continue ')
        print('              HORSES:')
        print('1. Ghost')
        print('2. Grace')
        print('3. Max ')
        print('4. Joey')
        print('5. Jamal')
        while True:
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
        time.sleep(1.5)
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
            x=input('Press ENTER to continue ')
            print('\n')
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
                time.sleep(3)
                rb=2
                break
            else:
                print('Invalid Choice')
                continue
        if rb==1:
            continue
        else:
            break

            