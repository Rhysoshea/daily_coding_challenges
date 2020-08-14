"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:

    def __init__(self, dummy):
        self.dummy = dummy 

    def generateParentheses(self, n):
        def generate(p, left, right, ans=[]):

            if left: generate(p+'(', left-1, right)

            if right > left: generate(p+')', left, right-1)

            if not right:  ans += p, # this works same as following line notice the comma
            # if not right: ans += [p]

            return ans

        return generate('', n, n)


solve = Solution(0)

ans3 = [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
print(solve.generateParentheses(3))
# assert(solve.generateParentheses(3) == ans3)
