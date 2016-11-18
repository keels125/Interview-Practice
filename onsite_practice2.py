def pond_sizes(matrix):
    sizes = []
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):
            size = get_size(matrix, r, c)
            sizes.append(size)
    return sizes

def get_size(matrix, row, col):
    if (row<0 or col<0 or row>len(matrix) or
        col>len(matrix[row]) or matrix[row][col]!=0):
        return 0
    
    size = 1
    matrix[row][col] == -1 #mark visited
    for r in range(-1,2):
        for c in range(-1, 2):
            size+=get_size(matrix, row+r, col+c)

    return size



def highest(num):
    highest = 0
    str_num = str(num)

    for char in str_num:
        temp = int(str_num.replace(char, ""))
        if (temp > highest):
            highest = temp
    return highest


def change_vowels(word):
    i = 0
    j= len(word)-1

    word_arr = list(word)
    vowels = ['a', 'e', 'i', 'o', 'u']
    while (i<=j):
        if word[i] in vowels and word[j] in vowels:
            temp = word_arr[i]
            word_arr[i] = word_arr[j]
            word_arr[j] = temp

            i+=1
            j-=1

        elif (word[i] in vowels):
            j-=1
        elif (word[j] in vowels):
            i+=1
        else:
            i+=1
            j-=1

    return ''.join(word_arr)


def master_mind(guess, solution):
    counts = {}
    hits = 0
    pseudo = 0

    poss = ['R', 'G', 'B', 'Y']
    
    for i in range(0, 4):
        charg = guess[i]
        chars = solution[i]
        
        if charg in counts:
            counts[charg][0]+=1
        else:
            counts[charg] = [1, 0]

        if chars in counts:
            counts[chars][1]+=1
        else:
            counts[chars] = [0, 1]

        if guess[i]==solution[i]:
            hits+=1
            counts[chars][0]-=1
            counts[chars][1]-=1

    print(counts['G'])

    for char in poss:
        if counts[char][0] == counts[char][1]:
            pseudo+=counts[char][0]

        elif counts[char][0] > counts[char][1] and counts[char][1]!=0:
            pseudo+=(counts[char][0] - counts[char][1])

        print(pseudo)


    return hits, pseudo
        


def missing_one(arr):
    target = len(arr)+1
    target_sum=0
    for i in range(1, target+1):
        target_sum+=i
        
    actual_sum = sum(arr)

    return target_sum - actual_sum


def count_2s(n):
    count = 0
    for num in range(n+1):
        temp = str(num)
        for char in temp:
            if char=='2':
                count+=1
    return count


def masseuse(appts):
    DP = [None] * len(appts)
    for i in range(len(appts)):
        if i==0:
            DP[i] = 0
        else:
            DP[i] = max(appts[i]+DP[i-1], DP[i-1])

    l = len(DP)
    return DP[l-1]


def compress(string):
    count = 1
    final = ""
    for i in range(1, len(string)):

        if (i == len(string)-1 and string[i]==string[i-1]):
            final+=string[i]+str(count+1)

        elif (i == len(string)-1 and string[i]!=string[i-1]):
            final+=string[i-1]+str(count)+string[i]+'1'

        elif string[i]==string[i-1]:
            count+=1
        else:
            final+=string[i-1]+str(count)
            count = 1

    return final
        

def main():
    print(pond_sizes([[0, 2, 1, 0], [0,1,0,1],
                      [1,1,0,1],[0,1,0,1]]))


main()
    
