"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def solution(input,k):
    output = []
    input.reverse()
    while input:
        row = []
        len_row = 0
        while len_row < k:
            if not input:
                break
            if (len_row + len(input[0]) + 1) < k:
                word = input.pop()
                if not row:
                    row.append(word)
                    len_row += len(word)
                else:
                    row.append(" ")
                    row.append(word)
                    len_row += len(word) + 1
            else:
                break
        if len_row == k:
            # print(row)
            output.append(row)
        else:
            for i in range(k-len_row):
                # print(row, "1 added", ((2*i)+1)%(len(row)-1))
                row[((2*i)+1)%(len(row)-1)] += " "

        output.append("".join([i for i in row]))
    return output


def test (input, k, ans):
    print (solution(input,k)==ans)
    print(ans)
    # assert (solution(input,k) == ans)


input1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k1 = 16
ans1 = ["the  quick brown", # 1 extra space on the left
        "fox  jumps  over", # 2 extra spaces distributed evenly
        "the   lazy   dog"] # 4 extra spaces distributed evenly

# print(solution(input1,k1))

test(input1, k1, ans1)
