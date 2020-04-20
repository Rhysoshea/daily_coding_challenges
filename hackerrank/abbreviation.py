"""
https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming&h_r=next-challenge&h_v=zen


given string a of uppercase and lowercase letters and string b of uppercase letters, return whether it is possible to find b within a after changing to uppercase and removing letters as necessary
can only delete lowercase letters
"""

def solution(a,b):
    b = list(b)
    a = list(a)
    if len(a) == 0 and len(b) > 0:
        return "NO"
    grid = [[0]*(len(b)+1) for i in range(len(a)+1) ]

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if b[j-1] == a[i-1].upper():
                grid[i][j] = grid[i-1][j-1] + 1
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])
   
    for row in range(len(grid)):
        print (a[row-1], grid[row])
   
    for row in range(1,len(grid)):
        if grid[row] == grid[row-1]:
            if a[row-2].islower() and a[row-2].upper() == a[row-1]:
                continue
            if a[row-1] == " ":
                return "NO"
            if a[row-1].islower():
                continue
            print("here")

            return "NO"


    if grid[len(a)][len(b)] == len(b):
        return "YES"
    return "NO"

assert(solution('daBcd','ABC') == "YES")
assert(solution('dacd', 'ABC') == "NO")
assert(solution('LIT ','LIT') == "NO")
assert(solution('beFgH', 'EFG') == "NO")

assert(solution('afG', '') == 'NO')
assert(solution('af', '') == 'YES')
assert(solution('', 'BGS') == 'NO')


assert(solution('CTBRhHXT',  'CTBRHXT') == 'YES')
assert(solution('CTBRHhXT',  'CTBRHXT') == 'YES')
assert(solution('aAaAaaAAAaaa',  'AAAAA') == 'YES')

assert(solution(
    'RDDO',  'RDO') == 'NO')
