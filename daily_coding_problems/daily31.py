"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
def choose_min_max(a,b):
    if len(a) > len(b):
        return b, a
    return a, b

def solution(input1, input2):
    if not input1 or not input2:
        return 0
    min_in, max_in1 = choose_min_max(input1, input2)
    max_cross = 0
    max_in = (len(min_in)-1)*' ' + max_in1 + (len(min_in)-1)*' '
    for i in range(len(max_in)-len(min_in)+1):
        cross = 0
        for j in range(len(min_in)):
            # print (min_in[j], max_in[j+i])
            if min_in[j] == max_in[j+i]:
                cross += 1
            # print(cross)
        max_cross = max(max_cross, cross)
    # print(min_in)
    # print(max_cross)
    if (len(max_in1) - max_cross) > len(max_in1):
        return (len(min_in1))
    return (len(max_in1) - max_cross)



def test(input1, input2, ans):
    assert (solution(input1, input2) == ans)


# input1 = "kitten"
# input2 = "sitting"
# ans1 = 3
#
# test(input1, input2, ans1)
#
# input3 = "hellohowareyou"
# input4 = "hihowareyou"
# ans2 = 5
#
# test(input3, input4, ans2)

input5 = "sitting"
input6 = "good"
ans3 = 9

test(input5, input6, ans3)

input7 = ""
input8 = ""
ans4 = 0

test(input7, input8, ans4)
