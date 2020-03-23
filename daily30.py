"""
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle. e.g.
#W#
###

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
e.g.
     #
     #
#WW#W#
#WW#W#
#W##W#
"""

def solution(input):
    if not input:
        return 0
    _min = min(input[0], input[-1])
    area = _min * len(input)
    walls = 0
    for i in input:
        if i <= _min:
            walls += i
        else:
            walls += _min
    return area - walls


def test(input, ans):
    assert (solution(input) == ans)

input1 =[2, 1, 2]
input2 = [3, 0, 1, 3, 0, 5]

test(input1, 1)
test(input2, 8)
