#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
# def check_anagram(s1,s2):
#     print (s1, s2)
#     first = {}
#     second = {}
#     for i in range(len(s1)):
#         if s1[i] not in first:
#             first[s1[i]] = 1
#         else:
#             first[s1[i]] = first[s1[i]] +1
#         if s2[i] not in second:
#             second[s2[i]] = 1
#         else:
#             second[s2[i]] = second[s2[i]] +1

#     if first != second:
#         return False
#     return True
    # s1 = [x for x in s1]
    # s2 = [x for x in s2]
    # s1.sort()
    # s2.sort()
    # if s1 != s2:
    #     return False
    # return True
    # for i in s1:
    #     if s1.count(i) != s2.count(i):
    #         return False
    # return True

# def sherlockAndAnagrams(s):
#     count = 0
#     for j in range(1,len(s)):
#         for i in range(0,len(s)-j):
#             for k in range(i+1, len(s)-j+1):
#                 if check_anagram(s[i:i+j], s[k:k+j]):
#                     count += 1
#     return count



def strhash(s):
    h = 0
    for c in s:
        # print (c," hash ",hash(c))
        # hash is a built-in python function that returns an integer hash
        h += hash(c)
    return(h)

def seqsum(n):
    # this is returning n choose 2 values because its keeping track of how many substrings have the same hash. If they have the same hash then they have the same letters and length, therefore there are n choose 2 permutations in these matches that produce anagrams 
    # print(n, " seqsum ", int((n**2 + n) / 2))
    return int((n**2 + n) / 2)

def sherlockAndAnagrams(s):
    count = 0
    for l in range(len(s)):
        counter = dict()
        #l is length of substr.
        for i in range(len(s)-l):
            hashed = strhash(s[i:i+l+1])
            if hashed not in counter:
                counter[hashed] = 1
            else:
                counter[hashed] += 1
        for k,v in counter.items():
            if v > 1:
                count += seqsum(v-1)
    print(count)
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input())
    q = 1
    for q_itr in range(q):
        # s = input()
        s = 'abba'
        result = sherlockAndAnagrams(s)
        print(result)
        # fptr.write(str(result) + '\n')

    # fptr.close()
