"""
Minimum Absolute Difference in an Array

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

return an integer that is the minimum of the absolute differences between all pairs in an array 

"""

def solution(arr):
    min = float("inf")
    arr.sort()
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        # print(diff)
        if  diff < min:
            min = diff
    # print(min)
    return min


assert (solution([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]) == 1)
