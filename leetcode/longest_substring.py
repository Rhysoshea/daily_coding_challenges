# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


# naive approach
# def lengthOfLongestSubstring(s):
#     if len(s) < 1:
#             return 0
#     max_l = 1
#     for i in range(len(s)):
#         letters = []
#         letters.append(s[i])
#         j = i+1
#         l = 1
#         if j > len(s)-1:
#             break
#         while s[j] not in letters and j <= len(s)-1:
#             letters.append(s[j])
#             l += 1
#             j += 1
#             if j > len(s)-1:
#                 break

#         max_l = max(max_l, l)
#     return max_l

# using a rolling window and set
# def lengthOfLongestSubstring(s):
#     # max_l = 0
#     if len(s) < 1:
#         return 0
#     i = 0
#     j = 1
#     letters = set(s[i])
#     max_l = len(letters)

#     while j < len(s):
#         if s[j] not in letters:
#             letters.add(s[j])
#             max_l = max(max_l, len(letters))
#             j +=1
#         else:
#             letters.remove(s[i])
#             i += 1

#     # print (max_l)
#     return max_l

# using a hashtable
def lengthOfLongestSubstring(s):
    max_l = 0
    h = {}
    if len(s) < 1:
        return 0
    i = 0
    j = 0

    while j < len(s):
        # print (h)
        if s[j] in h:
            i = max(i, h[s[j]])
        max_l = max(max_l, j-i+1) #registering the index of the last time a letter was seen
        h[s[j]] = j+1
        j+=1

    # print (max_l)
    return max_l

s = "abcabcbb"
assert(lengthOfLongestSubstring(s) == 3)

s = "pwwkew"
assert(lengthOfLongestSubstring(s) == 3)

s = "bbbb"
assert(lengthOfLongestSubstring(s) == 1)

s = ""
assert(lengthOfLongestSubstring(s) == 0)

s = " "
assert(lengthOfLongestSubstring(s) == 1)
