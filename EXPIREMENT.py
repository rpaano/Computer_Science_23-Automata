#Romel Paano

input1 = []
input2 = []
input3 = ''
count = 0
indi = 0
ind2 = 0
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
        #print(check2[ctr1])
        if check2[ctr1] == ' ':
            #print(check2)
            check2 = check2[:ctr1] + '' + check2[ctr1+1:]
            #print(check2)
        else:

            ctr1 += 1

    #print(check2)
    return check2


def second():
    global input1
    global input2
    global input3
    global count
    global indi
    global ind2
    
    while count < len(input1):
        #print("here6")
        #print("ind2", ind2, "indi", indi)
        #print(input1[count],input2,count)
        if input1[count] == input2 and indi >= 0:
            #print("here7")
            ind2 = ind2 + 1
            #print("ind2", ind2)
            input1= input1[:count] + input3 + input1[count+1:]
            count += 1
        elif indi < 0 and ind2 != 0:
            #print("here10")
            break
        elif input1[count] == ')':
            #print("here9")
            #print(ind2)
            indi -= 1
            count += 1
        elif input1[count] == '(':
            #print("here8")
            #print(ind2)
            indi += 1
            count += 1
        else:
            #print("here11")
            count += 1

        #print(indi, ind2)
        
        
        #print(input1)
    #print(indi)    

def main():
    global input1
    global input2
    global input3
    global count
    global indi
    global ind2

    input2 = input("Enter dummy variable: ")
    input3 = input("Enter what to change in too: ")

    if len(input2) != 1:
        return 1

    if len(input3) != 1:
        return 1

    if check_if(input2) == 1:
        return 1

    if check_if(input3) == 1:
        return 1

    while count < len(input1):
        #print("here")
        if input1[count] == 'L':
            #print("here1")
            count += 1
            while True:
                #print("here2")
                if input1[count] == input2:
                    #print("here3")
                    #print(count)
                    second()
                    break
                elif input1[count] == '.':
                    #print("here4")
                    break
                else:
                    count += 1
        #elif input1[count] == '(':
        #    count += 1
        #    indi += 1
        #elif input1[count] == '(':
        #    count += 1
        #    indi -= 1
        else:
            #print("here5")
            count += 1

        indi = 0
        ind2 = 0
            
    

    #print(input1)
    




input1 = input("Enter expression: ")
input1 = space(input1)

if check_if(input1) == 0:
    if main() == 1:
        print("NO CONVERSION!!!!")
    else:
        print("ANSWER: ",input1)

#if input1[count] != '(':
#    input1 = '(' + input1 + ')'

