"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""

def solution(input, regex):
    regex_alpha = ''.join([x for x in regex if x.isalpha()])
    if not regex_alpha in input:
        return False

    regex_split = regex.split(regex_alpha)
    input_split = input.split(regex_alpha)
    # print (regex_split)
    # print (input_split)

    for i, j in zip(regex_split, input_split):
        if not len(i) == len(j):
            if '*' in i:
                if '.' in i:
                    return False
                continue
            return False

    return True

def test(input, regex, ans):
    assert (solution(input, regex) == ans)



str1 = "ray"
regex1 = "ra."
str2 = "raymond"

regex2 = ".*at"
str3 = "chat"
str4 = "chats"
str5 = "at"
regex3 = ".at"
regex4 = "*at."

print (solution(str4, regex2))

test(str1, regex1, True)
test(str2, regex1, False)
test(str3, regex2, True)
test(str4, regex2, False)
test(str5, regex2, False)
test(str5, regex3, False)
test(str4, regex4, True)
test(str3, regex3, False)
test(str3, regex4, False)
