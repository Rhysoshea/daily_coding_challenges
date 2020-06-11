# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# using dictionary (as hash table)
def two_sum(arr, target):
    h = {}

    for i,num in enumerate(arr):
        n = target - num
        if n in h:
            return [h[n], i]
        else:
            h[num] = i

# using array - slower
# def two_sum(arr, t):
#     dp_arr = []

#     for i,num in enumerate(arr):
#         if num in dp_arr:
#             return [dp_arr.index(num), i]
#         else:
#             dp_arr.append(t-num)




arr = [2,7,11,15]
t = 9

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t = 9

print(two_sum(arr, t))