import sys

def dotProduct():
    data = []
    dot = 0
    for line in sys.stdin:
        data.append(line.split())

    k = int(data[0][0])
    n = int(data[0][1])

    d = {}
    for i in range(1,k+1):
        key = data[i][0]
        value = int(data[i][1])
        d[key] = value

    for j in range(k+1, n+k+1):
        key = data[j][0]
        value = int(data[j][1])
        if d.get(key):
            dot+= (value*d.get(key))
    print(dot)
        


def string(string):
    count = 0
    prev_char = ""
    new_string = ""
    for char in string:
        if count == 2:
            new_string+='e'
            count = 0
            prev_char = char

        elif (count == 1) and char!='e':
            new_string+='e'
            prev_char = char
            count = 0

        elif char == 'e' and prev_char!='e':
            count+=1
            
        elif char!='e':
            new_string+=char
            prev_char = char

    return new_string


print(string("aeiou"))
