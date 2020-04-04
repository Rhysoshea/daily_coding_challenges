'''
Problem
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal(which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers Mi, 1, Mi, 2 ..., Mi, N. Mi, j is the integer in the i-th row and j-th column of the matrix.

Output
# x: k r c, where x is the test case number (starting from 1), k is the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of columns of the matrix that contain repeated elements.
For each test case, output one line containing Case

Limits
Test set 1 (Visible Verdict)
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 100.
1 ≤ Mi, j ≤ N, for all i, j.

Sample

Input       Output

3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1     Case  # 1: 4 0 0

4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2     Case  # 2: 9 4 4

3
2 1 3
1 3 2
1 2 3       Case  # 3: 8 0 2

# 1, the input is a natural Latin square, which means no row or column has repeated elements. All four values in the main diagonal are 1, and so the trace (their sum) is 4.
In Sample Case

In Sample Case  # 2, all rows and columns have repeated elements. Notice that each row or column with repeated elements is counted only once regardless of the number of elements that are repeated or how often they are repeated within the row or column. In addition, notice that some integers in the range 1 through N may be absent from the input.

In Sample Case  # 3, the leftmost and rightmost columns have repeated elements.

'''
# def solution(n,arr):
#     k=r=c=0
#     keys = zip([f'{x}' for x in range(n)], ["" for x in range(n)])
#     dict_col = dict(keys)
#     dict_row = dict(keys)
#     bool_col = dict(keys)
#     bool_row = dict(keys)
#     print (dict_col)
#     exit()

#     for i in range(n):
#         for j in range(n):
#             num = arr[i][j]
#             if i==j:
#                 k+=num
#             if num not in dict_col[f'{j}']:
#                 dict_col[j].append(num)
#             elif num in dict_col[j]:
#                 if not bool_col[j]:
#                     c += 1
#                     bool_col[j] = True
#             if num not in dict_row[i]:
#                 dict_row[i].append(num)
#             elif num in dict_row[i]:
#                 if not bool_row[i]:
#                     r += 1
#                     bool_row[i] = True

#     return k,r,c


def solution(n, arr):
    k = r = c = 0

    for i in range(n):
        if len(arr[i]) != len(set(arr[i])):
            r += 1
        print([x[i] for x in arr], set([x[i] for x in arr]))
        if len([x[i] for x in arr]) != len(set([x[i] for x in arr])):
            c+=1
        k+=arr[i][i]

    return k, r, c

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = []
        for _ in range(n):
            a = [int(x) for x in input().strip().split()]
            arr.append(a)
        k, r, c = solution(n, arr)
        print("Case #{}: {} {} {}".format(i+1, k,r,c))
