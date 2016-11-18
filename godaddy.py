def rearrangeWord(word):
    l = len(word) -1
    result = word[:l] + word[l]
    print(result)
    for i in range(l, 0, -1):
        temp = word[:i-1] + word[i] + word[i-1]
        if len(result)!=l+1:
            temp+=word[i+1:]
        if temp < result and temp > word:
            result = temp
        
        #else continue
    if result > word:
        return result
    else:
        return "no answer"


print(rearrangeWord("xy"))
