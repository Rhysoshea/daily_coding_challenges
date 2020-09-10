"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

This pattern
|  /|  /|
| / | / |
|/  |/  |

| /| /|
|/ |/ |

gap between columns is 2*(rows-1)
"""


class Solution:

    def __init__():
        pass 

    # def convert (s, numRows):
    #     l = len(s)
    #     if l <= 1 or numRows == 1:
    #         return s 

    #     big_gap = 2*(numRows-1)
    #     little_gap = 0
    #     output = ""

    #     r = 0
    #     c = 0
    #     while r < numRows:
    #         i = r
    #         output += s[i]

    #         while i < l:
    #             i += big_gap
    #             if i < l and r != numRows-1:
    #                 output += s[i]
    #             i += little_gap 
    #             if i < l and r!= 0 :
    #                 output += s[i]

    #         r += 1
    #         big_gap -= 2
    #         little_gap += 2


    #     # print (output)

    #     return output 

    # alternate solution
    # equivalent to walking along zig zag 
    def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)): # creates a list of strings, each representing a row
            outp[lin] += s[i]  
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows - 1: # changes direction when reaching first or last row
                    pl *= -1
        # print (outp)
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr

solve = Solution 

# solve.convert("PAYPALISHIRING", 4)
solve.convert("123456789", 2)
