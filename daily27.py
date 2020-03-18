"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
def solution(input):
    stack = []
    open = ["{", "(", "["]
    close = ["}", ")", "]"]

    matcher = dict(zip(close,open))

    for i in input:
        # print (stack)
        if i in open:
            stack.append(i)
        elif i in close:
            if not stack:
                return False
            if stack.pop() != matcher.get(i):
                return False

    return len(stack) == 0


def test(input, ans):
    assert (solution(input) == ans)


input1 =  "([])[]({})"
input2 = "([)]"
input3 = "((()"


test(input1, True)
test(input2, False)
test(input3, False)
