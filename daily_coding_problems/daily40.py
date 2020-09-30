# Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

# Do this in O(N) time and O(1) space.



def solution(arr):
    result_arr = [0] * 32

    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            result_arr[i] = (result_arr[i] + bit) %3
        print (result_arr)

    result = 0
    for i, bit in enumerate(result_arr):
        if bit:
            result += 2 ** i

    return result

print(solution([6,1,6,6]))