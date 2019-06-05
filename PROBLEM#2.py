#Romel Paano


input1 = []
input2 = []
input3 = ""





def main():
    global indi
    global input1
    global input2
    input2 = input("Enter the second lamda:")
    input3 = input("Enter what dummy varaible:")
    count = 0
    while count < len(input1):
        if input1[count] == 'L':
            while count < len(input1):
                if input1[count] == input3:
                    input1= input1[:count] + input2 + input1[count+1:]
                    print(input1)
                    count += len(input3)
                elif input1[count] == ')' :
                    break
                else:
                    count += 1

                
        else:
            count += 1
    print(input1)
                
        
    
    

input1 = input("Enter the first lamda:")    

main()
