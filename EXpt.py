#Romel Paano

input1 = []
input2 = []
output = []
count = 0
out = 0 
leter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u''w','v','x','y','z']

def check_if(check1):

    lamda = 0
    paren = 0
    charac = 0
    ctr = 0
    inn = 0
    la = 0
    
    while ctr < len(check1):
        #print("here")
        #print(check1[ctr])
        if check1[ctr] == '(':
            #print("here1")
            la -= 1
            paren += 1
            if check1[ctr+1] != 'L':
                charac += 1
        elif check1[ctr] == ')':
            #print("here2")
            if paren == 0 or la == 1:
                #print("here3")
                return 1
            else:
                #print("here4")
                paren -= 1
                #charac += 1

        elif check1[ctr] == 'L':
            #print("here5")
            la -= 1
            lamda += 1
            charac += 1
        elif check1[ctr] == '.':
            #print("here6")
            if lamda == 0 or la == 1:
                #print("here7")
                return 1
            else:
                #print("here8")
                lamda -= 1
                la = 1
                #charac += 1
        else:
            charac += 1
            inn += 1

        #print(check1[ctr])
        
        if charac == 1:
            #print("here9")
            ctr3 = 0
            if inn == 1:
                #print("here12")
                inn -= 1
            else:
                #print("here13")
                ctr += 1
                
            while ctr3 < len(leter):
                #print("here10")
                if leter[ctr3] == check1[ctr]:
                    la = 0
                    #print("here11")
                    charac -= 1
                    break


                ctr3 += 1

                if ctr3 == len(leter):
                    #print("here11")
                    return 1
            

            
        ctr += 1

    #print(la)
    if la == 1:
        return 1
    
    if lamda == 1:
        return 1

    if paren == 1:
        return 1

    return 0

        
def space(check2):
    
    ctr1 = 0

    while ctr1 < len(check2):
        #print(input1[ctr1])
        if check2[ctr1] == ' ':
            #print(input1)
            check2 = check2[:ctr1] + '' + check2[ctr1+1:]
            #print(input1)
        else:

            ctr1 += 1


    return check2
            
def check():
    global input1

    ctr = 0
    ctr2 = 0
    
    while ctr < len(input1)-1:
        if input1[ctr] == 'L':
            #print(ctr, ctr2)
            ctr += 1
            letter = input1[ctr]
            #print(letter,input1[ctr])
            #print("L")

            ctr += 1

            ctr2 = ctr

            #print(ctr, ctr2)
            
    
            while ctr2 < len(input1)-1:
                #print("here2")
                #print(ctr2)
                if letter == input1[ctr2]:
                    return 1
                elif input1[ctr2] == '.':
                    #print(ctr2,len(input1))
                    while ctr2 < len(input1)-1:
                        #print(ctr2,input1[ctr2])
                        ctr2 += 1
                        if input1[ctr2] == 'L':
                            break
                
                ctr2 += 1
        
        ctr += 1
        
    return 0
            
def second():
    global input1 
    global input2 
    global count

    key = 0

    while True:
        if input1[count] == '(':
            count += 1
        elif input1[count] == 'L':
            break
        else:
            return 1

        
    if input1[count] == 'L':
        count += 1
        letter = input1[count]
        input1 = input1[:count-1] + '' + input1[count+2:]
        count -= 1
        #print("input1 ",input1 ,"count", count)
        while count < len(input1):
            #print("input1[count]", input1[count])
            if input1[count] == 'L':
                #print("here1")
                while True:
                    if input1[count] == '.':
                        #print("here2")
                        break
                    #print("")
                    #print(input1[count],count)
                
                    count += 1
            else:
                key += 1

            
            #print("input[count]", input1[count]) 
            if input1[count] == '.' or key != 0:
                #print("here4")
                while count < len(input1):
                    #print("here5")
                    if letter == input1[count]:
                        #print("here6")
                        input1 = input1[:count] + input2 + input1[count+1:]
                        count += len(input2)
                        
                    elif input1[count] == 'L':
                        #print("here7")
                        break

                    count += 1
            else:
                count += 1
            #print("lenght",len(input1))
            #print(input1[count])
    return 0

def expand():
    global input1

    ctr = 0
    
    while ctr < len(input1):

        if input1[ctr] == 'L' and input1[ctr+2] != '.':
            input1 = input1[:ctr+2] + '.' + input1[ctr+2:]
            input1 = input1[:ctr+3] + 'L' + input1[ctr+3:]

        ctr += 1
    

def main():
    global input1 
    global input2 
    global count
    global out
    global output

    
    input2 = input("Enter parameter expression: ")

    if input2[count] != '(' and len(input2) != 1:
        input2 = '(' + input2 + ')'

    input1 = space(input1)
    if check_if(input1) == 1:
        out += 1
        print("NO CONVERTION!!!")
        return 1

        
    input2 = space(input2)
    if check_if(input2) == 1:
        print("NO CONVERTION!!!")
        out += 1
        return 1
    
    

    #print(input2)

    if check() == 0:
        expand()
        if second() == 0:
             print("ANWER: ", input1)
        else:
            out += 1
            print("NO CONVERTION!!!")
         
    else:
        out += 1
        print("NO CONVERTION!!!")



input1 = input("Enter expression: ")



while True:
    count = 0
    main()
    if out != 0:
        break
















    
