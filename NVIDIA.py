#interview prep

def moveZeroes(lst):
    if len(lst)==0:
        return lst
    count = 0 #logic: count the # of non-0 elements and move to beginning

    for i in range(0, len(lst)):
        if (lst[i]!=0):
            lst[count]=lst[i] #move to front
            count+=1
    for j in range(count, len(lst)):
        lst[j]=0
        
    return lst

def reverse(string):
    rev=""
    str = string.split()
    n=len(str)-1
    while (n>=0):
        rev+=str[n]+" "
        n-=1
    return rev


def compress(string):
    current=string[0]
    count=1
    final=""

    for i in range(1, len(string)):
        if string[i]==current:
            count+=1
            
        else:
            final+=str(count)+current
            current=string[i]           
            count=1
    final+=str(count)+current #append the last one
    return final

def main():
    #print(moveZeroes([0,1,0,3,12]))
    #print(reverse("I am Keely"))
    print(compress("AAABBCCCCCCAAAAA"))



main()
