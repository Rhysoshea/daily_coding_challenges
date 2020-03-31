"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""

def solution(dict_input, str_input):
    positions = []
    for word in dict_input:
        print(word)
        for i, letter in enumerate(str_input):
            if word == str_input[i:i+len(word)]:
                positions.append((word,i))
    positions = sorted(positions, key=lambda x:x[1])
    print(positions)
    if not positions:
        return ""
    if sum([len(x[0]) for x in positions]) > len(str_input):
        new_positions = []
        current_length = 0
        print('here')
        for i, tuple in enumerate(positions):
            # print (positions[i+1][1])
            if current_length > positions[i+1][1]:
                continue
            new_positions.append(tuple[0])
            current_length += len(tuple[0])
            if (i+1) == len(positions):
                new_positions.append(positions[i+1][0])
                i +=1
    return [x[0] for x in positions]

def test(input, str, ans):
    assert (solution(input, str) == ans)


dict1 = {'quick',
         'brown',
         'the',
         'fox'}

str1 = "thequickbrownfox"
ans1 = ['the', 'quick', 'brown', 'fox']

dict2 = {'bed',
         'bath',
         'bedbath',
         'and',
         'beyond'}

str2 = "bedbathandbeyond"
ans2 = ['bedbath', 'and', 'beyond']
ans2 = ['bed', 'bath', 'and', 'beyond']

print (solution(dict2, str2))


# test(dict1, str1, ans1)
# test(dict2, str2, ans2)
