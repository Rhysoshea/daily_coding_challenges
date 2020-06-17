"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^(31) − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:

    def __init__():
        pass 

    def reverse(x):

        if x >= 2**31-1 or x <= -2**31 :
            return 0

        output = 0
        neg = False 
        if x < 0:
            neg = True 
            x *= -1

        while x != 0:
            
            r = x%10
            x = x//10
            output = output*10 + r 

        if output >= 2**31-1 or output <= -2**31: #32 bit integer also applies to output
            return 0
        if neg:
            output *= -1
        # print (output)
        return (output)



solve = Solution
assert (solve.reverse(123) == 321)
assert (solve.reverse(-123) == -321)
assert (solve.reverse(0) == 0)
assert (solve.reverse(1) == 1)
