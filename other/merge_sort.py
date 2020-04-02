"""
Practice merge sort
"""
def mergeSort(arr):
    if len(arr) < 2:
        return arr
    n = len(arr)//2
    arr1 = mergeSort(arr[:n])
    arr2 = mergeSort(arr[n:])
    sortedArr = []
    while arr1 and arr2:
        if arr1[0] > arr2[0]:
            sortedArr.append(arr2[0])
            arr2.pop(0)
        else:
            sortedArr.append(arr1[0])
            arr1.pop(0)
    if arr1 and not arr2:
        sortedArr.extend(arr1)
    if arr2 and not arr1:
        sortedArr.extend(arr2)
    print (sortedArr)
    return sortedArr


arr = [8,3,5,6,2,4,9,7,10,1]

print(mergeSort(arr))
