#coinbase interview question

def parser(string):
    stack1=[]

    #assume no whitespace

    for i in range(0, len(string)): #set up first stack
        if (string[i]=='(' or string[i]=='{' or string[i]=='['):
            stack1.append(string[i])
            
        else:
            popped=stack1.pop()
            if ((string[i]==']' and popped!='[') or (string[i]==')' and popped!='(')
                or (string[i]=='}' and popped!='{')):

                return False
    
    if not stack1: #not empty = true
        return True
    else:
        return False

def main():
    print(parser("({})["))

main()
