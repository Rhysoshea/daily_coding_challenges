# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

# You may assume each element in the array is distinct.

# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

def mergeSort(left, right):
    counter = 0
    newArr = []
    while left and right:
        if right[0] < left[0]:
            newArr.append(right[0])
            del right[0]
            counter += len(left)
        else:
            newArr.append(left[0])
            del left[0]

    newArr.extend(left)
    newArr.extend(right)

    return newArr, counter

def solution (arr, counter):
    if len(arr)==1:
        return arr,0

    n = len(arr)//2

    leftArr,leftCount = solution(arr[:n], counter) 
    rightArr,rightCount = solution(arr[n:], counter)

    newArr, add = mergeSort(leftArr, rightArr)
    counter=add+leftCount+rightCount

    return newArr, counter


print (solution([5,4,3,2,1], 0))
print (solution([2,4,1,3,5], 0))