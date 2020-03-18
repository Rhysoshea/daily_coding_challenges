'''
Given an array of queries, for every query check if it exists in the strings array
'''
def matchingStrings(strings, queries):

    return [True if x in strings else False for x in queries]


assert matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']) == [True, True, False]
