"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""

def solution(input_arr, k):
    output_arr = []
    i = 0
    while i+k <= len(input_arr):
        output_arr.append(max(input_arr[i:i+k]))
        i += 1
    return output_arr

def solution2(input_arr, k):
    output_arr = []
    queue = []
    for i in range(k):
        queue.append(input_arr[i])
    output_arr.append(max(queue))
    while k < len(input_arr):
        queue.pop(0)
        queue.append(input_arr[k])
        output_arr.append(max(queue))
        k += 1
    return output_arr

def test():
    assert (solution([10,5,2,7,8,7], 3) == [10,7,8,8])

input_arr = [10,5,2,7,8,7]
k = 3
print (solution2(input_arr,3))
test()
