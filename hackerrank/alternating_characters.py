"""
Alternating characters
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen


Function Description
return an integer representing the minimum number of deletions to make the input string alternating between A and B

For example, given the string AABAAB, remove an A at positions 0 and 3 to make ABAB in 2 deletions.

strings will only consists of A or B

"""

def solution (s):
    s = list(s)
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count


assert (solution("AABAAB") == 2)
assert (solution("AAAA") == 3)
assert (solution("BBBBB") == 4)
assert (solution("ABABABAB") == 0)
assert (solution("BABABA") == 0)
assert (solution("AAABBB") == 4)


