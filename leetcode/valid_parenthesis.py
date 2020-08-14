"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""

class Solution:

    def __init__(self, dummy):
        self.dummy = dummy

    def isValid(self, s):

        hash = {
            "[":"]",
            "(":")",
            "{":"}"
        }

        stack = []

        for i in range(len(s)):
            if s[i] in ["[", "(", "{"]:
                stack.append(hash[s[i]])
            else:
                if not stack or s[i] != stack.pop():
                    return False 

        if stack:
            return False 

        return True

solve = Solution(0)

assert(solve.isValid("()") == True)
assert(solve.isValid("()[]{}") == True)
assert(solve.isValid("(]") == False)
assert(solve.isValid("([)]") == False)
assert(solve.isValid("{[]}") == True)
assert(solve.isValid("") == True)
assert(solve.isValid("[") == False)
assert(solve.isValid("]") == False)
