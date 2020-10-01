# An sorted array of integers was rotated an unknown number of times.

# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

# You can assume all the integers in the array are unique.

# doesn't work if list is sorted, assuming rotation has happened
def search(arr, num):

    i = len(arr)//2
    dist = i//2 #jumps around at first and narrows down progressively

    while True:
        if arr[i] == num:
            return i
        elif arr[i] > arr[0] and arr[i-1] > arr[i]:
            break
        elif arr[i] > arr[0]:
            i = i + dist 
        elif arr[i] > arr[i-1]:
            i = i - dist 
        elif dist == 0:
            break 
        else:
            break 
        dist = dist//2


    # now perform binary search with offset of i applied
    low = i
    high = i - 1
    dist = len(arr)//2


    while True:

        if dist == 0:
            return None
        
        x = (low + dist) % len(arr)

        if arr[x] == num:
            return x

        if arr[x] < num:
            low = (low + dist) % len(arr)
        elif arr[x] > num:
            high = (len(arr) + high - dist) % len(arr) 
        dist = dist//2






print (search([13,18,25,2,8,10], 8))
print (search([13,18,25,27,81,100], 81))