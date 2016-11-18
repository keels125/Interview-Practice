l = []
l.append(["set", "a", 10])
l.append(["set", "b", 30])
l.append(["set", "a", 15])
print(l)

def findName(index, name):
    for i in range(index, -1, -1):
        print(l[i][0], l[i][1])
        if (l[i][0] == "set" and l[i][1] == name):
            return str(l[i][2])
    return "not found"

n = len(l) -1

print(findName(n-1, "a"))
        
