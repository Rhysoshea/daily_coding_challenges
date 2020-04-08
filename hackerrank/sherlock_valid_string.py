"""
sherlock and the valid string

https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Return weather a string is valid or not
Valid if every letter in string has same frequency or if removing one character then all have same frequency

"""


def solution(str):
    checked = dict()
    for i in list(str):
        if i in checked:
            continue
        checked[i] = str.count(i)
    one = False
    vals = list(checked.values())
    print(vals)
    
    for i in range(len(vals)-1):
        this = vals[i]
        next = vals[i+1]
        if this != next:
            if abs(next-this) > 1:
                return "NO"
            if abs(next-this) == 1:
                if one:
                    return "NO"
                else:
                    one = True 

    return "YES"

assert (solution("abc") == "YES")
assert (solution("abcc") == "YES")
assert (solution("abccc") == "NO")
assert (solution("aabbcd") == "NO")
