def solvePuzzle(num):
    holes = {'0': 1,'4': 1, '6':1, '8':2, '9':1}
    n = str(num)
    total = 0
    if n[0] == '-':
        new_num = n[1:]
    else:
        new_num = n
    for char in new_num:
        if (int(char)%2==0 and char!='2') or char=='9':
            total+=holes[char]

    return total




##def match(matchtype, left, right):
##    results = []
##    if matchtype == "left":
##        for i in range(len(left)):
##            notfound = False
##            for j in range(len(right)):
##                if left[i]==right[j]:
##                    results.append([i, j])
##                    notfound = True
##            if not notfound:
##                results.append([i, -1])
##
##    elif matchtype == "right":
##        for i in range(len(right)):
##            notfound = False
##            for j in range(len(left)):
##                if left[j]==right[i]:
##                    results.append([j, i])
##                    notfound = True
##            if not notfound:
##                results.append([-1, i])
##    elif matchtype == "inner":
##        for i in range(len(left)):
##            for j in range(len(right)):
##                if left[i]==right[j]:
##                    results.append([i, j])
##
##    else:
##        print("invalid matchtype")
##
##            
##
##    return results



























print(match("inner", ["apple", "grape", "melon", "grape"],
            ["grape", "lemon", "apple"]))
