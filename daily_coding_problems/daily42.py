# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def solution(arr, t):
    arr.sort()

    newArr = [x for x in arr if x<=t]
    newArr.reverse()
    # print (newArr)
    sum = 0
    stack = []
    j=0
    for i in range(len(newArr)):
        sum += newArr[i]
        stack.append(newArr[i])

        for k in range(j+i+1,len(newArr)):
            sum += newArr[k]
            stack.append(newArr[k])
            print (stack)
            if sum>t:
                del stack[-1]
                sum-= newArr[k]
                continue

            elif sum==t:
                return stack

        sum=0
        stack=[]
        j+=1

    return None



print (solution([7,1,4,5,12,2],10))