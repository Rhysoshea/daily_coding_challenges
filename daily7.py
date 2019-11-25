'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.


'''

"""
Every branch calls itself recursively twice, so our runtime is O(2**n)
"""

def num_encodings1(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1:
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings1(s[2:])

    total += num_encodings1(s[1:])
    return total


"""
Using dynamic programming
each iteration takes O(1), the whole algorithm now takes O(n)
"""

from collections import defaultdict

def num_encodings2(s):
    cache = defaultdict(int)
    cache[len(s)] = 1

    for i in reversed(range(len(s))):
        # print i
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i+2]
            cache[i] += cache[i+1]
    return cache[0]

if __name__ == "__main__":
    print (num_encodings1('211'))
    print (num_encodings2('211'))
