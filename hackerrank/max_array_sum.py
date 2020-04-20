"""
https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

return the maximum subset sum for a given array of non-adjacent numbers

"""

def solution(arr):
    if len(arr) < 4:
        if len(arr) == 3:
            return max(arr[0]+arr[2], arr[1])
        if len(arr) == 2:
            return max(arr[0], arr[1])
        return arr[0]
    # cumulative array to keep track of the total sums
    cumArr = [0]*len(arr)
    cumArr[0] = arr[0]
    cumArr[1] = max(arr[1], cumArr[0])

    for i in range(2,len(arr)):
        cumArr[i] = max(cumArr[i-2]+arr[i], max(cumArr[i-1], arr[i]))
    # print(cumArr)
    return cumArr[len(cumArr)-1]


# assert (solution([3, 5, -7, 8, 10]) == 15)
# assert (solution([2, 1, 5, 8, 4]) == 11)

assert (solution([-10,-5,-4,-2,-1]) == 11)
