"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:

    def __init__():
        pass 

    # def longestCommonPrefix(strs):

    #     if len(strs) < 1 or "" in strs:
    #         return ""
    #     i = 0
    #     proceed = True
    #     while proceed and i < min([len(x) for x in strs]):
    #         check = strs[0][i]
    #         for word in strs:
    #             if check != word[i]:
    #                 proceed = False
    #                 i -= 1

    #                 break
    #         i += 1



        # print(strs[0][:i])
        return strs[0][:i]

    # alternative writing
    def longestCommonPrefix(strs):

        prefix = ""
        if len(strs) == 0: return prefix 

        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i]==c for a in strs):
                prefix += c
            else:
                break 
        return prefix

solve = Solution

assert(solve.longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
assert(solve.longestCommonPrefix(["dog", "racecar", "car"]) == "")
assert(solve.longestCommonPrefix([]) == "")
assert(solve.longestCommonPrefix([""]) == "")
assert(solve.longestCommonPrefix(["a"]) == "a")
