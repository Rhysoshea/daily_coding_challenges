def quicksort(arr, lo, hi):
    if lo<hi:
        pi = partition(arr, lo, hi)
        quicksort(arr, lo, pi-1)
        quicksort(arr, pi+1, hi)

def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def partition(arr, lo, hi):
    i = lo-1 
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] < pivot:
            i+=1
            swap(arr,i,j)
    swap(arr,i+1,hi)
    return i+1