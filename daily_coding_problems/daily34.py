"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle"

"""
def solution(input):
    r_input = input[::-1]
    i = 0
    if input == r_input:
        return input
    while i < len(input):
        # print (input[:-i])
        # print (r_input[i:])
        # i+=1
        if input[:-i] != r_input[i:]:
            i+=1
        else:
            break

    if i >= len(input)-1:
        return min(r_input[:i] + input, input + r_input[len(input)-i:])

    return r_input[:i] + input

def test(input, ans):
    assert(solution(input) == ans)


input1 = "race"  #racecar
ans1 = "ecarace"

input2 = "google" #googlelgoog
ans2 = "elgoogle"

input3 = "racecar"
ans3 = "racecar"

test(input1, ans1)
