'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''


class Solution:

    def __init__(self):
        pass 

    # def longestPalindrome(self, s):
    #     if len(s) < 1:
    #         return s
    #     if s.count(s[0]) == len(s):
    #         print (s)
    #         return s

    #     max_p = ""

    #     n = len(s)
    #     i = 0
    #     while i < n:
    #         if i == 0:
    #             if s[0] == s[1]:
    #                 max_p = s[0:2]
    #         j = 0 
    #         while i - j >= 0 and i + j < n:
    #             # print (s[i-j], s[i+j])
    #             # print (j)
    #             if s[i-j] == s[i+j]:
    #                 if len(s[i-j:i+j+1]) > len(max_p):
    #                     max_p = s[i-j:i+j+1]
    #                 j += 1
    #             elif s[i] == s[i+1]:
    #                 if len(s[i:i+2]) > len(max_p):
    #                     max_p = s[i:i+2]
    #                 break
    #             else:
    #                 break
    #         i += 1

    #     print (max_p)
    #     return max_p

    # def longestPalindrome(self, s):
    #     if len(s) < 1:
    #         return s
    #     if s.count(s[0]) == len(s):
    #         # print(s)
    #         return s

    #     max_p = ""

    #     n = len(s)
    #     i = 0
    #     while i < n:

    #         try:
    #             if s[i] == s[i+1]:
    #                 j = 0
    #                 while s[i-j] == s[i+j+1]:
    #                     j += 1
    #                     if i+j+1 >= n or i-j < 0:
    #                         break
    #                 # print(j)

    #                 if len(s[i-j+1:i+j+1]) > len(max_p):
    #                     max_p = s[i-j+1:i+j+1]

    #             if s[i-1] == s[i+1]:
    #                 j = 0
    #                 while s[i-j-1] == s[i+j+1]:
    #                     j += 1
    #                     if i+j >= n or i-j-1 < 0:
    #                         break 
    #                 if len(s[i-j:i+j]) > len(max_p):
    #                     max_p = s[i-j:i+j+1]
    #             if len(s[i]) > len(max_p):
    #                 max_p = s[i]
    #             i += 1
    #         except: 
    #             break

    #     # print(max_p)
    #     return max_p

    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                # print(s[i:j][::-1])
                if len(m) >= j-i:  # To reduce time
                    break
                
                elif s[i:j] == s[i:j][::-1]: #checks if substring is equal to substring in reverse 
                    m = s[i:j]
                    break
        return m

solve = Solution 



assert(solve.longestPalindrome(1, "babad") == "bab")
assert(solve.longestPalindrome(1, "cbbd") == "bb")
assert(solve.longestPalindrome(1, "sa") == "s")
assert(solve.longestPalindrome(1, "bb") == "bb")
assert(solve.longestPalindrome(1, "ccd") == "cc")
assert(solve.longestPalindrome(1, "a") == "a")
assert(solve.longestPalindrome(1, "aaaaaa") == "aaaaaa")
assert(solve.longestPalindrome(1, "tattarrattat") == "tattarrattat")
