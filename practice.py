#unique path 1

def unique_path(m, n): #m x n grid
    dp = [[0 for x in range(n)] for x in range(m)]
    dp[0][0]=1
    
    for i in range(0, m):
        dp[i][0]=1
    for j in range(0, n):
        
        dp[0][j]=1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j]=dp[i][j-1]+dp[i-1][j]

    return dp[m-1][n-1]

def unique_path2(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for x in range(n)] for x in range(m)]
    dp[0][0]=1
    
    for i in range(0, m):
        if (grid[i][0]==1):
            dp[i][0]=0
        else:
            dp[i][0]=1
    for j in range(0, n):
        if (grid[0][j]==1):
            dp[0][j]==0
        else:
            dp[0][j]=1

    for i in range(1, m):
        for j in range(1, n):
            if (grid[i][j]==1):
                dp[i][j]==0

            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
    return dp[m-1][n-1]


def pairs(arr, dif):
    arr.sort()
    i=0
    j=1
    while (i<len(arr) and j<len(arr)):
        if (arr[j]-arr[i]==dif):
            print("Pair found: ", arr[i], ", ", arr[j], "\n")
            i=i+1
            

        elif (arr[j]-arr[i]<dif):
            j=j+1

        else:
            i=i+1
            if (i==j):
                j=j+1
def BooHoo(n):
    for x in range(0, n+1):
        if (x%3==0 and x%5==0):
            print("BooHoo")
        elif (x%3==0):
            print("Boo")
        elif (x%5==0):
            print("Hoo")
        else:
            print(x)
        #print("\n")

def getInversedNumber(n):
    b=bin(n)
    fin=""
    for x in range (2, len(b)):
        if b[x]=='1':
            fin=fin+'0'
        else:
            fin=fin+'1'
    fin='0b'+fin
    print(int(fin, 2))



def main():
    grid=[[1, 1], [0,1]]
    print(unique_path2(grid))
    #arr=[1, 12, 5, 3, 4, 2]
    #arr=[]
 #   pairs(arr, 2)
 #   getInversedNumber(50)
 #   BooHoo(16)
main()
