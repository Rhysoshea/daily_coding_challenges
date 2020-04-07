"""
Merge sort counting inversions

https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

Implement a merge sort and count how many inversions are performed
Bubblesort is more intuitive to use here but will not perform fast enough

Sample Input        Sample Output

2  
5  
1 1 1 2 2           0
5  
2 1 3 1 2           4

Solution:
implement merge sort and count everytime arr2 is smaller than arr1 
increment the count by the numbers remaining in arr1
"""

def mergeSort(arr, count):
    if len(arr) < 2:
        return arr, count
    arr1, count1 = mergeSort(arr[:len(arr)//2], count)
    arr2, count2 = mergeSort(arr[len(arr)//2:], count)

    i=j=0
    output = []
    while i < len(arr1) and j < len(arr2):
        if arr2[j] < arr1[i]:
            output.append(arr2[j])
            count += len(arr1)-i 
            j += 1
        else:
            output.append(arr1[i])
            i += 1
    if j < len(arr2):
        output.extend(arr2[j:len(arr2)])
    if i < len(arr1):
        output.extend(arr1[i:len(arr1)])

    count = count+count1+count2
    return output, count

def solution(n, arr):
    count = 0
    sortedArr, count = mergeSort(arr, count)
    # print (count)
    return count

assert (solution(5,[1,1,1,2,2]) == 0)
assert (solution(5, [2, 1, 3, 1, 2]) == 4)
