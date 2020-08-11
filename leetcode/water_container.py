"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    def __init__():
        pass 

    

    def maxArea(height):

        def calcMax(x,y):
            return (y-x) * min(height[x], height[y])

        x = 0 # start at beginning of list
        y = len(height)-1 # start at end of list

        maxA = calcMax(x,y)

        while x < y:

            if height[x] <= height[y]:
                if x+1 < y:
                    x+=1
                    maxA = max(maxA, calcMax(x,y))
                else:
                    break
            else:
                if y-1 > x:
                    y-=1
                    maxA = max(maxA, calcMax(x, y))
                else:
                    break
        return maxA

solve = Solution 

assert(solve.maxArea([1,8,6,2,5,4,8,3,7]) == 49)
assert(solve.maxArea([1,2,9,9,2,1]) == 9)
assert(solve.maxArea([1,2]) == 1)
assert(solve.maxArea([1,1,1,1,1,1]) == 5)
assert(solve.maxArea([2, 1, 11, 11, 1, 2]) == 11)
