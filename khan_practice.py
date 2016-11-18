

def subsetSum(S, goal):
    subsetSumArr = [[None for i in range(goal+2)] for j in range(len(S)+2)]

    for q in range(1, goal):
        print(q)
        subsetSumArr[q][0] = False

    for k in range(1, len(S)):
        subsetSumArr[0][k] = True
        


    for i in range(1, goal+1):
        for j in range(1, len(S)+1):
            subsetSumArr[i][j] = subsetSumArr[i][j-1]
            if (i >= S[j-1]):
                subsetSumArr[i][j] = subsetSumArr[i][j] or subsetSumArr[i - S[j-1]][j-1]
    return subsetSumArr[goal][len(S)]

        

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findNextLargest(root, node):
    nextLargest = root.data
    first_time = True
    
    if root is None:
        return 0

    stack = []
    stack.append(root)
    
    while(stack):
        print("here")
        curr = stack.pop()
        
        if (curr.data>node.data and curr.data<=nextLargest) or (curr.data>node.data and first_time):
            nextLargest = curr.data
            first_time= False

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return nextLargest


def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1

    x = 1
    y = 1

    fib = 0
    
    while (n>2):
        fib = x + y
        temp = y
        x = temp
        y = fib
        n-=1

    return fib

def fib_recurse(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib_recurse(n-1) + fib_recurse(n-2)



def main():
    print(subsetSum([3, 2, 7, 1], 6))


main()

    
