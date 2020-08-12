"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""


class Solution:

    def __init__():
        pass 

    # slow solution
    # def threeSumClosest(nums, target):

    #     diff = 1000000
    #     t = 0

    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             for k in range(j+1, len(nums)):
    #                 s = nums[i] + nums[j] + nums[k]
    #                 if abs(s-target) < diff:
    #                     t = s
    #                     diff = abs(s-target)
        
    #     return t

    # two pointer solution
    def threeSumClosest(nums, target):

        nums.sort()
        
        diff = 1000000
        t = 0
        i = lo = hi = 0
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1

            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(s-target) < diff:
                    t = s
                    diff = abs(s-target)
                if s > target:
                    hi -= 1
                elif s < target:
                    lo += 1
                else:
                    return target

        print (t)
        return t

solve = Solution 

assert(solve.threeSumClosest([-1,2,1,-4], 1) == 2)
assert(solve.threeSumClosest([10, 15, -21, 5], 7) == 4)

# -1  2  1  -4
#  3  0  1   6

# -21 5 10 15
#  28   2  3  8  
