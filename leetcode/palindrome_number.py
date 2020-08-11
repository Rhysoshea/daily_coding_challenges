"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
"""


class Solution:
    # solution allowing conversion to string
    def __init__():
        pass

    def isPalindrome(x):

        return str(x) == str(x)[::-1]

class Solution:
# solution without converting to string
    def __init__():
        pass

    def isPalindrome(x):

        if x < 0:
            return False 

        x_copy = x
        y=0

        while x_copy != 0:
            r = x_copy % 10
            y = y*10 + r
            x_copy = x_copy // 10

        if y == x:
            return True 
        return False

solve = Solution 
assert (solve.isPalindrome(121) == True)
assert (solve.isPalindrome(-121) == False)
assert (solve.isPalindrome(10) == False)
assert (solve.isPalindrome(0)== True)
assert (solve.isPalindrome(1)== True)
assert (solve.isPalindrome(-1)== False)
assert (solve.isPalindrome(12345678987654321)== True)
assert (solve.isPalindrome(12321)== True)
assert (solve.isPalindrome(1221) == True)
assert (solve.isPalindrome(12212)== False)
