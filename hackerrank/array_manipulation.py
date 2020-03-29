"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros n=10 . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices a and b inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next m lines contains three space-separated integers a,b  and k, the left index, right index and summand.

Constraints
3<=n<=10^7
1<=m<=20^5
1<=a<=b<=n
0<=k<=1)^9

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be 200.
"""
"""
Solution:
Use 'difference array' method

Instead of adding the values to all instances between a and b
Add value to arr[a] and subtract from a[b+1]
Also be sure to add in an extra index of n+1 because of this
What we end up with is an array keeping track of the relative difference between i and i+1
E.g.
in reality a final array could look like [10,20,20,25,5]
the difference array keeps track of this [10,10,0,5,-20]
Then we just need to add all the values and find what the peak of the sum is
         25
   20 20
10
            5
Answer = 25

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# time O(N)
# space O(N)

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for m in queries:
        a,b,k = m
        arr[a] = arr[a] + k
        if b < n:
            arr[b+1] = arr[b+1]-k
        # naive approach done in O(nm) time
        # for i in range(a-1,b):
        #     arr[i] = arr[i] + k
    maxi,x=0,0
    for i in arr:
        x = x+i
        if x > maxi:
            maxi = x
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
