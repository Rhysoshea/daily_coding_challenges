"""
making anagrams
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

return an integer of the number of deletions required to make two strings anagrams of each other

"""
import string

def solution(str1, str2):
    alpha = string.ascii_lowercase
    count = 0
    for letter in alpha:
        c1 = str1.count(letter)
        c2 = str2.count(letter)
        count += abs(c2-c1)
    # print (count)
    return count

str1 ="cde"
str2 = "abc"
assert (solution(str1, str2) == 4)

str1 = "cde"
str2 = "dcf"
assert (solution(str1, str2) == 2)
