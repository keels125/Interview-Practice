#interview practice

##def num_dif(str1, str2):
##    if (abs(len(str1)-len(str2))>1): #if lengths differ by more than 1
##        return False
##    min_len=min(len(str1), len(str2))
##    print(max_len)
##
##    i=0 #str1
##    j=0 #str2
##
##    count=0 #hold num difs
##
##    while (i!=min_len and j!=min_len):
##        if (str1[i]==str2[j]):
##            i+=1
##            j+=1
##        else if (str1[i]!=str2[j]):
##            count+=1
##            if (count>1):
##                return False
##            else:
                

def fib(n):
    x=1 #n-2
    y=1 #n-1
    if (n==0 or n==1):
        return 1
    
    res=0
    i=2
    
    while (i<=n):
        res=x+y
        x=y
        y=res
        i+=1

    return res
        

def main():
    for i in range (0, 8):
        print(fib(i))


main()
