#Romel Paano

from random import randint

letter = ['a','b','c','d']
lamda = ['L', '.']
indi = 0


def lam():
    print(lamda[0],end='')

def dot():
    print(lamda[1],end='')

def lett():
    print(letter[randint(0,3)],end='')



def main():
    global indi
    leng = randint(1,30)
    indi = 0
    #print(leng)
    if leng == 1:
        LAMDA = randint(0,3)
        print(letter[LAMDA],end='')

    elif leng == 2:
        if randint(1,2) == 1:
            count = 0 
            while count < 2:
                LAMDA = randint(0,3)
                print(letter[LAMDA],end='')
                count += 1
        else:
            count = 0 
            while count < 2:
                print(lamda[count],end='')
                print(letter[count],end='')
                count += 1

    else:
        count = 0 
        while count < leng:
            if randint(1,2) == 1:
                if indi == 0:
                    lam()
                    indi += 1
                    lett()
                    count += 1
                elif indi == 1:
                    dot()
                    indi -= 1
                    lett()
                    count += 1
                
                ''''if count + 1 == leng && :
                    dot()
                    indi -= 1
                    lett()
                    count+=1'''
            else:
                lett()
                count +=1

ctr = 0                
while ctr < 20:
    print()
    print(ctr)
    main()
    ctr += 1
