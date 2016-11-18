def anagrams(words):
    words[0] = ''.join(sorted(words[0]))
    prev = words[0]
    
    for i in range(1, len(words)):
        words[i] = ''.join(sorted(words[i]))
        if words[i]!=prev:
            return False
        else:
            prev = words[i]

    return True
        

def anagrams2(words):
    ascii_arr = [0] * 256
    
    for char in words[0]:
        ascii_arr[ord(char)] += 1

    temp = list(ascii_arr)

    for i in range(1, len(words)):
        for char in words[i]:
            temp[ord(char)]-=1
            if temp[ord(char)] < 0:
                return False

        if not check_zeroes(temp):
            print(i)
            return False

        temp = list(ascii_arr)

    return True


def check_zeroes(l):
    for i in range(0, len(l)):
        if l[i]!=0:
            return False

    return True


def createPalindrome(string):
    d= {}
    even = False
    if len(string)%2==0:
        even = True
        
    for char in string:
        if char in d:
            d[char]+=1
        else:
            d[char]=1

    num_odds = 0
    for entry in d:
        if d[entry]%2!=0:
            if num_odds==0 and even==False:
                num_odds+=1
            else:
                return False

    return True



def sumStrings(num1, num2):
    result = ""
    min_num = min(len(num1), len(num2))-1
    diff = max(len(num1), len(num2)) - min_num - 1

    while min_num>=0:
        add = int(num1[min_num])+int(num2[min_num])
        result = str(add) + result
        print(result)
        min_num-=1

    if len(num1)>len(num2):
        for i in range(diff-1, -1, -1):
            result = str(num1[i]) + result
    elif len(num2)>len(num1):
        for i in range(diff-1, -1, -1):
            result = str(num2[i]) + result
    else:
        return str(result)


    return str(result)
def main():
    print(sumStrings("1234", "456"))
        
main()
