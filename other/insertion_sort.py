"""
practice insertion sort

"""

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 

def insertionSort(arr):
    for i in range(1, len(arr)):
        k=i
        for j in range(i-1, -1, -1):
            while arr[k] < arr[j]:
                swap(arr, k,j)
                k-=1
    return arr 

#alternative
def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


arr = [8, 3, 5, 6, 2, 4, 9, 7, 10, 1]
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertionSort(arr))
