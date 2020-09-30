# given an array A of N integers, return the smallest positive integer (greater than 0) that does not occur in A

def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort()
    if A[-1] <= 0:
        return 1
    if len(A) == 1:
        if A[0] < 1:
            return 1
        if A[0] == 1:
            return 2
        return 1
        
    i=0
    
    while A[i] <= 0:
        i+=1
    
    k = 1

    for j in range(i,len(A)):
        if A[j] > k:
            return k
        k+=1

    return A[-1]+1
# tests

assert(solution([1,2,3,4]) == 5)
assert(solution([0,0,0]) == 1)
assert(solution([-1,0,1]) == 2)
assert(solution([-4,-1,-3]) == 1)
assert(solution([1]) == 2)
assert(solution([0]) == 1)
assert(solution([2]) == 1)
assert(solution([10]) == 1)
assert(solution([1,2,3,4,0,-1,-3,-4]) == 5)
assert(solution([2,3,4,0,-1,-3,-4]) == 1)
assert(solution([-1000000,1000000]) == 1)
assert(solution([103,105,158,130]) == 1)
assert(solution([1, 3, 6, 4, 1, 2]) == 5)
