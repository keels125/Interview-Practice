def one_away(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    if abs(len1-len2)>1:
        return False

    i=0
    j=0
    difs=0

    while (i<len1 and j<len2):
        if difs>1:
            return False
        elif (string1[i]==string2[j]):
            i+=1
            j+=1
        else:
            if (len1==len2):
                difs+=1
                i+=1
                j+=1
            elif len1>len2:
                i+=1
            else:
                j+=1
    return True


def palindrome(string):
    i = 0
    j = len(string)-1

    string = string.upper()

    while (i<=j):
        if not (string[i].isalpha()):
            i+=1
        elif not (string[j].isalpha()):
            j-=1
        else:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
            
    return True



def seq_sum(arr):
    sum = arr[0]

    for i in range(1, len(arr)):
        
        if (i!=len(arr)-1):
            if (sum+arr[i]>0):
                print(i, sum)
                sum+=arr[i]
            else:
                sum = 0
    return sum


def find_char(string1, string2):
    mins = None
    maxs= None

    if (len(string1)<len(string2)):
        mins = string1
        maxs = string2
    else:
        mins = string2
        maxs = string1

    i=0
    j=0

    while (i<len(mins) and j<len(mins)):
        if string1[i]!=string2[j]:
            return maxs[i]
        
        else:
            i+=1
            j+=1

    #if not found yet, must be last char
    return maxs[i]






def sorted_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])
    r = rows-1
    c = cols-1

    final = []
    start = arr[rows-1][cols-1]

    while(start!= arr[0][0]):
        final.append(start)
        for i in range(rows, 0):
            for j in range(cols, 0):
                if arr[i-1][j]<=arr[i][j-1]:
                    final.append(arr[i-1][j])
                else:
                    final.append(arr[i][j-1])

        start = arr[r-1][c-1]
        r-=1
        c-=1

    final.append(arr[0][0])
    return final

    
    






def main():
    print(sorted_matrix([[30, 25], [20, 15], [10, 5]]))


main()
                
