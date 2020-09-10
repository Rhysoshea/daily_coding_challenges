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
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    
    def __init__():
        pass 

    def intToRoman(num):

        remainder = num
        factors = []

        dict_symbols = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        divisors = list(dict_symbols.keys())
        n = 0
        while remainder != 0:
            current = divisors[n]
            while remainder >= current:

                factors.append(current)
                remainder -= current
            n += 1

        print (factors)

        return "".join([dict_symbols[x] for x in factors])

solve = Solution

assert(solve.intToRoman(6) == "VI")
assert(solve.intToRoman(1) == "I")
assert(solve.intToRoman(9) == "IX")
assert(solve.intToRoman(18) == "XVIII")
assert(solve.intToRoman(58) == "LVIII")
assert(solve.intToRoman(1994) == "MCMXCIV")
