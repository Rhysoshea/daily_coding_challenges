'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

'''

def distinct_char(s,k):
    if k == 0:
        return 0

    bounds = (0,0)
    h = {}
    max_length = 0
    for i,char in enumerate(s):
        h[char] = i
        if len(h) <= k:
            new_lower_bound = bounds[0]
        else:
            key_to_pop = min(h, key=h.get)
            new_lower_bound = h.pop(key_to_pop) + 1

        bounds = (new_lower_bound, bounds[1]+1)
        max_length = max(max_length, bounds[1]-bounds[0])

    return max_length


k = 2
s = "abcba"

print (distinct_char(s,k))
