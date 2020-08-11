"""

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

"""

# class Solution:

#     def __init__():
#         pass 

#     def romanToInt(s):

#         total = 0

#         symbolDict = {
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000
#         }
#         i = 0
#         while i < len(s):

#             l = s[i]

#             if i+1 < len(s):
#                 next = s[i+1]
#             else:
#                 next = "None"
#             if l == "I" and next == "V":
#                 total += 4
#                 i += 2
#             elif l == "I" and next == "X":
#                 total += 9
#                 i += 2
#             elif l == "X" and next == "L":
#                 total += 40
#                 i += 2
#             elif l == "X" and next == "C":
#                 total += 90
#                 i += 2
#             elif l == "C" and next == "D":
#                 total += 400
#                 i+= 2
#             elif l == "C" and next == "M":
#                 total += 900
#                 i += 2
#             else:
#                 total += symbolDict[l]
#                 i += 1

#         # print (total)
#         return total


class Solution:

    def __init__():
        pass 

    def romanToInt(s):

        symbolDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = [symbolDict[i] for i in s if i in symbolDict] # convert everything to integer first

        # for each number, if it is greater than the next then add
        # if the number is lower than the next then subtract
        return sum( [ i if i>=n[min(j+1, len(n)-1)] else -i for j,i in enumerate(n) ] )

solve = Solution 

assert(solve.romanToInt("III") == 3)
assert(solve.romanToInt("IV") == 4)
assert(solve.romanToInt("IX") == 9)
assert(solve.romanToInt("LVIII") == 58)
assert(solve.romanToInt("MCMXCIV") == 1994)
