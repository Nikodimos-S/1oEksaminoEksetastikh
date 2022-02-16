import random
import collections

#check for winning conditions horizontally and vertically
def hv_check():
    #horizontal checks
    if (('o' in aa) and ('o' in ab) and ('o' in ac)) or (('0' in aa) and ('0' in ab) and ('0' in ac)) or (('O' in aa) and ('O' in ab) and ('O' in ac)):
        return True
    elif (('o' in ba) and ('o' in bb) and ('o' in bc)) or (('0' in ba) and ('0' in bb) and ('0' in bc)) or (('O' in ba) and ('O' in bb) and ('O' in bc)):
        return True
    elif (('o' in ca) and ('o' in cb) and ('o' in cc)) or (('0' in ca) and ('0' in cb) and ('0' in cc)) or (('O' in ca) and ('O' in cb) and ('O' in cc)):
        return True
    #vertical Checks
    elif (('o' in aa) and ('o' in ba) and ('o' in ca)) or (('0' in aa) and ('0' in ba) and ('0' in ca)) or (('O' in aa) and ('O' in ba) and ('O' in ca)):
        return True
    elif (('o' in ab) and ('o' in bb) and ('o' in cb)) or (('0' in ab) and ('0' in bb) and ('0' in cb)) or (('O' in ab) and ('O' in bb) and ('O' in cb)):
        return True
    elif (('o' in ac) and ('o' in bc) and ('o' in cc)) or (('0' in ac) and ('0' in bc) and ('0' in cc)) or (('O' in ac) and ('O' in bc) and ('O' in cc)):
        return True 
    else:
        return False   
#diagonal checks
def dg_check():
    if (('o' in aa) and ('o' in bb) and ('o' in cc)) or (('0' in aa) and ('0' in bb) and ('0' in cc)) or (('O' in aa) and ('O' in bb) and ('O' in cc)):
        return True
    elif (('o' in ca) and ('o' in bb) and ('o' in ac)) or (('0' in ca) and ('0' in bb) and ('0' in ac)) or (('O' in ca) and ('O' in bb) and ('O' in ac)):
        return True
    else:
        return False

#checking if a spcae in the 3x3 board is already full
def sqr_check(a):
    return collections.Counter(choice_list)==collections.Counter(a)


sum=0
for i in range(0,100):
    #making the lists for the board
    aa=[]
    ab=[]
    ac=[]
    ba=[]
    bb=[]
    bc=[]
    ca=[]
    cb=[]
    cc=[]

    r1=[aa,ab,ac]
    r2=[ba,bb,bc]
    r3=[ca,cb,cc]
    choice_list=['o','0','O']
    turns=0             #turns counter for final results
    win=False
    while win==False:
        cords=random.randrange(1,10)
        if cords==1:
            if sqr_check(aa):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in aa):
                    choice=random.choice(choice_list)
                aa.append(choice)
                turns=turns+1
                if hv_check() or dg_check:
                    win=True
        elif cords==2:
            if sqr_check(ab):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in ab):
                    choice=random.choice(choice_list)
                ab.append(choice)
                turns=turns+1
                if hv_check():
                    win=True
        elif cords==3:
            if sqr_check(ac):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in ac):
                    choice=random.choice(choice_list)
                ac.append(choice)
                turns=turns+1
                if hv_check() or dg_check():
                    win=True
        elif cords==4:
            if sqr_check(ba):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in ba):
                    choice=random.choice(choice_list)
                ba.append(choice)
                turns=turns+1
                if hv_check():
                    win=True
        elif cords==5:
            if sqr_check(bb):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in bb):
                    choice=random.choice(choice_list)
                bb.append(choice)
                turns=turns+1
                if hv_check() or dg_check():
                    win=True
        elif cords==6:
            if sqr_check(bc):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in bc):
                    choice=random.choice(choice_list)
                bc.append(choice)
                turns=turns+1
                if hv_check():
                    win=True
        elif cords==7:
            if sqr_check(ca):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in ca):
                    choice=random.choice(choice_list)
                ca.append(choice)
                turns=turns+1
                if hv_check() or dg_check():
                    win=True
        elif cords==8:
            if sqr_check(cb):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in cb):
                    choice=random.choice(choice_list)
                cb.append(choice)
                turns=turns+1
                if hv_check():
                    win=True
        elif cords==9:
            if sqr_check(cc):
                cords=random.randrange(1,10)
            else:
                choice=random.choice(choice_list)
                while (choice in cc):
                    choice=random.choice(choice_list)
                cc.append(choice)
                turns=turns+1
                if hv_check() or dg_check():
                    win=True
    sum=sum+turns
print("The average number of turns to end the game was:",sum/100)


    
