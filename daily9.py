'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

'''
Quick and easy way, but done in O(2**n) time
'''
# def largest_sum(list):
#     if not list:
#         return 0
#     return (max(largest_sum(list[1:]), list[0] + largest_sum(list[2:])))

'''
Use dynamic programming to store values as we go
'''
# def largest_sum(list):
#     if len(list) <= 2:
#         # return 0 if there is no list otherwise it is one of 2 numbers
#         return max(0, max(list))
#
#     # setup cache, 0s for each number in list
#     cache = [0 for i in list]
#     cache[0] = max(0, list[0])
#     cache[1] = max(cache[0], list[1])
#
#     for i in range(2, len(list)):
#         num = list[i]
#         cache[i] = max(cache[i-2] + num, cache[i-1])
#     return (cache[-1])

'''
Can do this in less space since only the last 2 numbers of cache are used
So use variables instead of cache
'''
def largest_sum(list):
    if len(list) <= 2:
        # return 0 if there is no list otherwise it is one of 2 numbers
        return max(0, max(list))

    max_excluding_last = max(0, list[0])
    max_including_last = max(max_excluding_last, list[1])

    for num in list[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_excluding_last, max_including_last)


print (largest_sum([2, 4, 6, 2, 5]))
