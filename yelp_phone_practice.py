from random import randint

def randomMines(m, n, mines):
    board = [[False for i in range(m+1)] for j in range(n+1)] #col x row

    points = []
    
    for i in range(m):
        for j in range(n):
            points.append([i, j])

    print(points)

    for k in range(mines+1):
        index = randint(0, len(points)-1)
        print(points[index])
        board[points[index][0]][points[index][1]] = True
        points.remove(points[index])

    for line in board:
        print(line)



def reverseWords(string):
    words = string.split()
    result = ""
    for i in range(len(words)):
        words[i] = str(reversed(words[i]))
        

    return ''.join(words)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node


def reverseList():
    head = Node(3)
    head.next = Node(4)
    head.next.next = Node(5)
    head.next.next.next = Node(6)
    LList = LinkedList(head)

    curr = head
    prev = None

    while (curr is not None):
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n

    LList.head = prev

    foo = LList.head
    while (foo is not None):
        print(foo.data)
        foo = foo.next


def kPairs(l, k):
    l = sorted(l)

    i = 0
    j = len(l)-1

    while (i<j):
        if ((l[i]+l[j]) == k):
            print([l[i], l[j]])
            i+=1
            j-=1

        elif (l[i]+l[j] < k):
            i+=1

        else:
            j-=1



def groupAnagram(l):
    d = {}

    for word in l:
        s = ''.join(sorted(word))
        d[s] = []

    for word in l:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)

    for entry in d:
        print(d[entry])



def colorSort(l):
    counter = [0,0,0]
    for color in l:
        counter[color]+=1

    sort = []
    j = 0
    for color in counter:
        for i in range(color):
            sort.append(j)
        j+=1
    return sort

print(colorSort([2, 2, 1, 0, 1, 0, 2, 1, 1, 2, 0]))


    
        
                  
                  




