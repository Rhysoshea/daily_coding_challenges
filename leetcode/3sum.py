"""

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def __init__():
        pass 

    def threeSum(nums):
       
        triplets = set()
        nums.sort()

        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1

            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    triplets.add(tuple([nums[i], nums[lo], nums[hi]]))
                    lo += 1
                    hi -= 1

        return triplets



solve = Solution 

# assert(solve.threeSum([-1,0,1,2,-1,-4]) == [[-1,0,1], [-1,-1,2]])
assert(solve.threeSum([0,0,0,0]) == [[0,0,0]])
assert(solve.threeSum([1, -1, 1, -1, 1]) == [])
assert(solve.threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]])
