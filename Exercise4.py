import random
win1 = 0
win2 = 0
draw=0
for nikodimos in range(0,100):#run without any cheating involved
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        win2=win2+1
    else:
        '''
        sxolia pollwn
        grammwn
        '''
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            win1=win1+1
        elif sum2>sum1:
            win2=win2+1
        else:
            draw=draw+1
print("Player1 won ",win1," times out of 100, while Player 2 won ",win2," times and drew ",draw," times")
win1=0
win2=0
draw=0
for nikodimos in range(0,100):#run completely 100% fairly and with no cheeating or anything unfair like that
    xartia = []
    cheatcards=[]
    figures = ["J", "Q", "K"]
    cheatlist = ["J", "Q", "K",10]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    for i in cheatlist:
        for j in color:
            cheatcards.append([i,j])
    random.shuffle(xartia)
    random.shuffle(cheatcards)
    player1=[]
    sum1=0
    runs1=0
    while sum1<16:
        sum1=0
        if runs1==0:#giving player one his advantage
            cheat=cheatcards.pop()
            player1.append(cheat)
            xartia.remove(cheat)
            runs1=runs1+1
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        win2=win2+1
    else:
        '''
        sxolia pollwn
        grammwn
        '''

        player2=[]
        sum2=0
        runs2=0
        while sum2<16:
            sum2=0

            while runs2==0 and (xartia[-1]in cheatcards):
                random.shuffle(xartia)
                runs2=1
            
            player2.append(xartia.pop())
            #print(player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            win1=win1+1
        elif sum2>sum1:
            win2=win2+1
        else:
            draw=draw+1
        
print("With the cheating involved Player1 won ",win1," timesout of 100 and Player2 won ",win2," times, while drawing",draw,"times.")
