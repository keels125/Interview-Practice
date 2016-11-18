def merge(list1, list2):

    i = 0
    j = 0

    sort = []

    while (i < len(list1) and j < len(list2)):
        if list1[i] < list2[j]:
            sort.append(list1[i])
            i+=1
        elif list1[i] > list2[j]:
            sort.append(list2[j])
            j+=1
        else:
            sort.append(list1[i])
            sort.append(list2[j])
            i+=1
            j+=1

    if i<len(list1):
        for idx in range(i, len(list1)):
            sort.append(list1[idx])
    elif j<len(list2):
        for idx in range(j, len(list2)):
            sort.append(list2[idx])

    return sort

print(merge([1, 2, 3, 4, 5] ,[4, 5, 6, 7, 8]))

    
