"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:

    def __init__(self,dummy):
        self.dummy = dummy 

    def removeDuplicates(self, nums):
        if len(nums) < 1:
            return 0
        i = 1
        last = nums[0]
        while i < len(nums):
            if nums[i] == last:
                del nums[i]
            else:
                last = nums[i]
                i+=1
        # print (nums)
        return len(nums)
    

solve = Solution(0)


assert(solve.removeDuplicates([1,1,2]) == 2)

assert(solve.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5)
