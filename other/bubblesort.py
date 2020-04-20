

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr 


arr = [8, 3, 5, 6, 2, 4, 9, 7, 10, 1]

print(bubbleSort(arr))
