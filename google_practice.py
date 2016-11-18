from math import floor
def perm_dups(s):
    a = set()
    perm_dups_helper(s, "", a, 0)
    print(a)

def perm_dups_helper(s, sofar, a, i):
    if (i == len(s)):
        a.add(sofar)
    else:    
        perm_dups_helper(s, sofar+s[i], a, i+1)
        perm_dups_helper(s, sofar, a, i+1)




def sparse_search(target, arr):
    #modified binary search
    #find mid

    def find_mid(arr, low, high):
        mid = floor((high - low)/2 -1)
        if (arr[mid] != ""):
            return mid
        find_mid(arr, low, mid-1)
        find_mid(arr, mid+1, high)

    low = 0
    high = len(arr)-1
    mid = find_mid(arr, low, high)
    print(mid)
        



def strob(string):
    i=0
    j=len(string)-1
    strobo = ['1', '8', '0', '6', '9']
    special = ['6', '9']

    while (i<=j):
        if (string[i] not in strobo or string[j] not in strobo):
            return False
        
        elif ((string[i]!=string[j]) or (string[i] in special or string[j] in special)):
            print("here")
            if ((string[i]=='6' and string[j]!='9' ) or
                (string[i]=='9' and string[j]!='6') or
                (string[i]!='6' and string[j]=='9') or
                (string[i]!='9' and string[j]=='6')):
                return False
        i+=1
        j-=1

        

    return True




def power(x, y):
    
    even = False #y even or odd
    if (y%2) == 0:
        even = True
    else:
        even = False
        
    if y==0:
        return 1
    elif y<0:
        return power_helper(1, x, abs(y), True, even) #true/false for neg, true/false for even/odd
    else:
        return power_helper(1, x, y, False, even)

def power_helper(curr, x, y, neg, even):
    if y==1:
        if (neg): #y is negative
            if (even):
                return 1/curr
            else:
                return 1/(curr*x) #multiply once more
        else:
            if (even):
                return curr
            else:
                return curr*x #multiply once more
        
    return power_helper(curr*(x*x), x, floor(y/2), neg, even)



def rotated(A, n):
    def modifiedBinarySearch(A, low, high):
        l = len(A)
        if low >= high:
            return -1
        if A[low]<=A[high]:
            return low
        mid = floor((low+high)/2)
        nextVal = (mid+1)%n
        previous = (mid-1+n)%n

        if (A[mid] <= A[nextVal] and A[mid] <= A[previous]):
            return mid
        elif A[mid]<=A[high]:
            return modifiedBinarySearch(A, low, mid)
        elif A[mid] >= A[low]:
            return modifiedBinarySearch(A, mid+1, high)

    def BinarySearch(A,n):
        l = len(A)
        low = 0
        high = l

        while (low<=high):
            mid = floor((high-low)/2 - 1)
            if (A[mid]>n):
                high = mid-1
            elif (A[mid]<n):
                low = mid+1
            else:
                return mid
                

    x = modifiedBinarySearch(A, 0, len(A)-1)

    leftArray = A[:x]
    rightArray = A[x:]

    if (n == rightArray[len(rightArray)-1]):
        return len(rightArray)-1

    elif (n > rightArray[len(rightArray)-1]):
        return BinarySearch(leftArray, n)
    else:
        return BinarySearch(rightArray, n)
      

def main():

    print(power(-2, 4))
    
main()
