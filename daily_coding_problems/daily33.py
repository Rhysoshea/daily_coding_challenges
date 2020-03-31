'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''
def solution(input):



def test(input, ans):
    assert (solution(input) == ans)

input1 = [2, 1, 5, 7, 2, 0, 5]
ans1 = "2\n1.5\n2\n3.5\n2\n2\n2"

print(solution(input1))


2    2
1 2    1.5
1 2 5   2
1 2 5 7   3.5
1 2 2 5 7   2
0 1 2 2 5 7    2
0 1 2 2 5 5 7    2
