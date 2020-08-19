"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters(just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


2 = a b c
3 = d e f
4 = g h i
5 = j k l
6 = m n o
7 = p q r s
8 = t u v
9 = w x y z

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:

    def __init__(self,dummy):
        self.dummy = dummy

    def letterCombinations(self, digits):

        if digits == "": return []

        alpha = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z']
            }

        text = [""]


        for i in range(len(digits)):
            letters = alpha[digits[i]]
            current_text = text
            text = []
            for j in range(len(current_text)):
                s = current_text[j]
                for k in range(len(letters)):
                    text.append(s+letters[k])
        # print (text)
        return text

solve = Solution(0)

assert (solve.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
assert (solve.letterCombinations("2") == ["a", "b", "c"])
