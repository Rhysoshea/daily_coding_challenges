# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.
import time

def powerSet(original):
    output = set([])

    if not original:
        return output 

    queue = []

    for i in original:
        queue.append(set([i]))


    while queue:
        # print (queue)
        current = queue[0]
        del queue[0]
        output.add(frozenset(current))
        for next in queue:
            # print (next)
            newList = list(current)+list(next)
            newSet = current.copy()
            newSet.update(next)
            if len(newSet) == len(newList):
                queue.append(newSet)

    return output

# using recursion 
def power_set(s):
    if not s:
        return [[]]
    result = power_set(s[1:])
    return result + [subset + [s[0]] for subset in result]



input = [1,2,3,4,5,6,7]

start = time.time()
powerSet(input)
print (time.time() - start)

start = time.time()
power_set(input)
print(time.time() - start)