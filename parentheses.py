def checkParen(string):
    stack = []

    for char in string:
        if char=='[' or char=='{' or char=='(':
            stack.append(char)

        else:
            top = stack.pop()
            if top=='[' and char!=']':
                return False

            elif top=='(' and char!=')':
                return False

            elif top=='{' and char!='}':
                return False

    if stack:
        return False
    else:
        return True


def palindrome(string):
    i = 0
    j = len(string)-1

    while (i<=j):
        if string[i]!=string[j]:
            return False
        else:
            i+=1
            j-=1
    return True

print(palindrome("racecar"))
print(palindrome("110011"))
print(palindrome("keely"))
