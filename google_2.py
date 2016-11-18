import random

def matrix_search(matrix, elt):
    row = 0
    col = len(matrix)-1

    while (row <= len(matrix)-1 and col>=0):
        if matrix[row][col] == elt:
            return True
        elif matrix[row][col] >= elt:
            col-=1
        else:
            row +=1
    return False


def smallest_dif(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    i = 0 #index into arr1
    j = 0 #index into arr2

    dif = abs(arr1[i]-arr2[j])
    
    while (i<len(arr1) and j<len(arr2)):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            if ((arr1[i] - arr2[j]) < dif):
                dif = arr1[i] - arr2[j]
            i+=1
            j+=1
    return dif

def multiply(num1, num2):
    result = 0
    if num2<0:
        num2 = abs(num2)
        for i in range(num2):
            result+=num1
            return multiply(-1, result)
    else:
        for i in range(num2):
            result+=num1
        return result

def subtract(num1, num2):
    return num1 + (multiply(-1, num2))

def sum_swap(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    
    arr1_sum = sum(arr1)
    arr2_sum = sum(arr2)

    find = abs(arr1_sum - arr2_sum)
    i = 0 #index into arr1 
    j = 0 #index into arr2

    while (i<=len(arr1) and j <= len(arr2)):
        if arr1[i]+arr2[j]==find:
            return [arr1[i], arr2[j]]
        elif arr1[i]+arr2[j]<find:
            if arr1[i]>=arr2[j]:
                i+=1
            else:
                j+=1
        else:
            return -1
    return -1


def pairs(arr, value):
    arr = sorted(arr)
    results = []
    i = 0
    j = len(arr)-1

    while (i<j):
        if arr[i] + arr[j] == value:
            results.append([arr[i], arr[j]])
            i+=1
            j-=1

        elif arr[i] + arr[j] < value:
            i+=1
        else:
            j-=1
    return results

def rand():
    r = random.randint(0, 4)
    return (r + 2) % 6


def main():
    print(rand())

main()
