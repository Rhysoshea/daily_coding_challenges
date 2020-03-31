'''
Given an array of integers, find the first missing positive integer in LINEAR TIME AND CONSTANT SPACE. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3                  [-1, 4, 3, 1]
                        [-1, 1, 3, 4]
                        [1, -1, 3, 4]
You can modify the input array in-place.
'''

def first_missing(array):
    for i, num in enumerate(array):
        while i+1 != array[i] and 0 < array[i] <= len(array):
            v = array[i]
            array[i] = array[v-1]
            array[v-1] = v
            if array[i] == array[v-1]:
                break
    for i, num in enumerate(array,1):
        if num != i:
            return i
    return len(array)+1

'''
This below method works but it is not in linear time and constant space. Having to sort every indice takes O(n log n) time.
Sort the array from lowest to highest
Check at each integer, n if the next one is +1 more, if not then return n+1
'''

def sort(unsorted):
    check = 0
    while True:
        for i in range(len(unsorted)-1):
            if unsorted[i] > unsorted[i+1]:
                x, y = unsorted[i], unsorted[i+1]
                unsorted[i], unsorted[i+1] = y, x
                check = 0
            else:
                check += 1
                if check == len(unsorted)-1:
                    return unsorted

def missing(array):
    ''' for each i in unsorted check if it is larger than i+1, if it is swap '''
    sorted = sort(array)
    print sorted
    for n in range(len(sorted)):
        if n == len(sorted) -1:
            if sorted[n] <= 0:
                return 1
            else:
                return sorted[n]+1
        elif ((sorted[n] + 1) != sorted[n+1]) and (sorted[n] + 1 > 0):
            return sorted[n] + 1
        else:
            pass



print (first_missing([3, 4, 2, 1]))
