'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example
sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

'''

def sort_array(source_array):
    odds = [x for x in source_array if x%2!=0]
    return [x if x%2==0 else odds.pop() for x in source_array ]

assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 32, 5, 8, 0]
assert sort_array([]) ==[]
# sort_array([5, 3, 2, 8, 1, 4])
