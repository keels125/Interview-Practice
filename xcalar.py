import sys
def maxThreats(a):
    size = len(a)

    threats = 0
    cols = []
    rows = []

    matrix = [[0 for x in range(size)] for y in range(size)]

    for i in range(size):
        row = i-1 #zero indexing
        col = a[i]-1 #zero indexing

        rows.append(row)
        cols.append(cols)

        matrix[col][row] = 1

    for j in range(size):
        for k in range(size):
             if matrix[j][k] == 1:
                temp=checkCol(matrix, j)
                if temp > threats:
                    threats = temp
    print(matrix)
    return threats

def checkCol(matrix, j):
    result = 0
    for i in range(0, j):
        if matrix[i][j] == 1:
            print("here 1")
            result+=1
    for i in range(j+1, len(matrix)):
        if matrix[i][j] == 1:
            print("here 2")
            result+=1
    return result
    






def stockMax():
    stocks = []
    for line in sys.stdin:
        inputs = line.split()
        stocks.append(inputs)
    print(stocks)





























                
            
    
print(stockMax())
    
