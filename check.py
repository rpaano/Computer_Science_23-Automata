#Romel Paano

from random import randint


let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u''w','v','x','y','z']

def lambdas():
    global lam

    lam.append('L')
    
def dot():
    global lam

    lam.append('.')

def opens():
    global lam

    lam.append('(')
    
def closes():
    global lam

    lam.append(')')


def main():
    global let
    global lam
    
    leng = randint(1,29)
    para = 0
    lam_dot = 0
    ctr = 0
    ok = 0
    okna = 0
    c = 0 

    if leng == 1:
        lam.append(let[randint(0,24)])
        return 0

    if leng == 2:
        if randint(0,1) == 0:
            lam.append(let[randint(0,24)])
            lam.append(let[randint(0,24)])
        else:
            lambdas()
            lam.append(let[randint(0,24)])
            dot()
            lam.append(let[randint(0,24)])
            return 0
    

    while ctr < leng:
        key = randint(1,3)

        if key == 1 and lam_dot  == 0:
            if para == 0:
                opens()
                para += 1
                c += 1
                if randint(2,3) == 3:
                    key = 3
                else:
                    key = 2
            elif para == 1 and okna == 1:
                okna -= 1
                closes()
                para -= 1
            elif okna != 0:
                key = 3
        if key == 2:
            if lam_dot == 0:
                lambdas()
                lam_dot += 1
                key = 3
            elif lam_dot == 1 and okna == 1:
                okna -= 1
                dot()
                lam_dot -= 1
                key = 3

        if key == 3:
            lam.append(let[randint(0,24)])
        
            
        

        ctr += 1

    if lam_dot == 1:
        dot()
        lam.append(let[randint(0,24)])

    if para == 1:
        closes()
        lam.append(let[randint(0,24)])

        
count = 0
        
while count < 20:
    lam = []
    main()

    print(count+1, end='\t')
    for s in lam:
        print(s,end='')

    print()
    count += 1


