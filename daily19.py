"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""
def solution1(input):
    #O(N*K^2) time by running through each row K times to check min (also K) i.e. 3 enumerations, N, K, K
    #O(NK) space same as input
    # i = house
    # j = colour
    cumulative_matrix = [[0 for y in x] for x in input]
    cumulative_matrix[0] = input[0]

    for i, house in enumerate(input):
        if i == 0:
            continue
        for j, cost in enumerate(house):
            cumulative_matrix[i][j] = min([x for ind,x in enumerate(cumulative_matrix[i-1]) if ind != j]) + cost
    return min(cumulative_matrix[-1])

def solution2(input):
    #O(N*K^2) time by running through each row K times to check min (also K) i.e. 3 enumerations, N, K, K
    #O(K) space as keeping track of 2 rows of length K
    # i = house
    # j = colour
    cumulative_last_row = input[0]

    for i, house in enumerate(input):
        if i == 0:
            continue
        cumulative_new_row = []
        for j, cost in enumerate(house):
            cumulative_new_row.append(min([x for ind,x in enumerate(cumulative_last_row) if ind != j]) + cost)
        cumulative_last_row = cumulative_new_row

    return min(cumulative_new_row)

def test(input, ans):
    assert (solution2(input) == ans)

input1 =  [[10, 20 ,30],
          [1,  2,  3 ],
          [15, 25, 35]]

input2 = [[10, 20],
          [1,  2],
          [15, 25],
          [5, 30]]

print (solution2(input1))

test(input1, 27)#10 + 2 + 15
test(input2, 51)#20 + 1 + 25 + 5

# [colour  1   2   3
#  house1 [10, 20 ,30],
#  house2 [1,  2,  3 ],
#  house3 [15, 25, 35]
#  ]
