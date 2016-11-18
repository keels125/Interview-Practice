def word_transform(word1, word2):
    print(word1)
    changed = []
    for i in range(len(word1)): #steps in process
        print(i)
        for j in range(len(word1)): #chars
            if j not in changed:
                word = word1[:j]+word2[j]+word1[j+1:]
                if word in open('words.txt').read():
                    word1= word
                    print("->", word1)
                    changed.append(j)
                    break
    print(changed)



def roman(roman):
    final = 0
    chars = {'I':1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while (i<len(roman)):
        num = chars[roman[i]]
        if num==1:
            if (i!=len(roman)-1 and roman[i+1]!='I'):
                final+=(chars[roman[i+1]]-1)
                i+=2
            else:
                final+=1
                i+=1
        else:
                final+=num
                i+=1

    return final


def max_sum(arr):
    dp = [None] * len(arr)
    for i in range(len(arr)):
        if i==0 or dp[i-1] <=0:
            dp[i] = arr[i]
        elif i!=0 and dp[i-1]>0:
            dp[i] = arr[i]+dp[i-1]

    return dp[len(arr)-1]


def max_sub(arr):
    n = len(arr)
    dp = [None] * n
    for i in range(n):
        if i==0:
            dp[i] = 0
        elif (i<n-1 and arr[i]>=arr[i+1]):
            dp[i]=0
        else:
            dp[i] = 1 + dp[i-1]

    return dp[n-1]

def steal_house(values):
    n = len(values)
    dp = [None] * n
    for i in range(n):
        if i==0:
            dp[i]=0
        else:
            dp[i] = max(values[i]+dp[i-2], dp[i-1])

    return dp[n-1]


def serialize(arr):
    serialized = ""
    for i in range(len(arr)):
        serialized += arr[i]
        l = len(arr[i])
        arr[i] = l
    print("serialized: ", serialized)
    return [serialized, arr]

def deserialize(arr):
    results = serialize(arr)
    new_arr = results[1]
    word = results[0]

    for i in range(len(new_arr)):
        temp = new_arr[i]
        new_arr[i] = word[:temp]
        word = word[temp:]
    print(new_arr)
    return new_arr



def find_word(arr, word):
    curr_char = 0
    visited = [[False for x in range(len(arr))] for y in range(len(arr[0]))]
    return find_word_helper(arr, word, visited, curr_char, 0, 0)

def find_word_helper(arr, word, visited, curr_char, r, c):
    if (check_visited(visited)):
        return False
    
    if (curr_char>=len(word)):
        return True
    
    if r<0 or r>len(arr) or c<0 or c>len(arr[0]):
        return False

    if arr[r][c] == word[curr_char]:
        visited[r][c] = True
        curr_char+=1
        adj = get_adj(arr, r, c)
        for index in adj:
            find_word_helper(arr, word, visited, curr_char, index[0], index[1])
    else:
        visited[r][c] = True
        adj = get_adj(arr, r, c)
        for index in adj:
            find_word_helper(arr, word, visited, curr_char, index[0], index[1])

                                

def get_adj(arr, r, c):
    adj = []
    if (arr[r-1][c]):
        adj.append([r-1, c])
    if (arr[r+1][c]):
        adj.append([r+1, c])
    if (arr[r][c-1]):
        adj.append([r, c-1])
    if (arr[r][c+1]):
        adj.append([r, c+1])
    if (arr[r+1][c+1]):
        adj.append([r+1, c+1])
    if (arr[r-1][c-1]):
        adj.append([r-1, c-1])
    if (arr[r-1][c+1]):
        adj.append([r-1, c+1])
    if (arr[r+1][c-1]):
        adj.append([r+1, c-1])
        
    return adj

def check_visited(arr):
    for sub in arr:
        for item in sub:
            if item==False:
                return False
    return True


def main():
    print(find_word([['s', 'f', 't'], ['d', 'a', 'h'],
                     ['r', 'y', 'o']], "rat"))


main()


