def findLargest(arr):

    temp = [arr[0], arr[1], arr[2]]
    
    first = max(arr[0], arr[1], arr[2])
    temp.remove(first)
    third = min(arr[0], arr[1], arr[2])
    temp.remove(third)
    second = temp[0]
        
    for i in range(3, len(arr)):
        elt = arr[i]
        if elt >= first:
            temp1 = first
            temp2 = second

            first = elt
            second = temp1
            third = temp2
            
        elif (elt < first and elt >= second):
            t = second
            second = elt
            third = t
        elif (elt < second and elt >=third):
            third = elt

    result = first+second+third

    print("Largest sum is: ", result)

findLargest([12, 34, 10, 6, 40])
