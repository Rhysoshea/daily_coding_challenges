'''
given a list of numbers and a number k, return whether any two numbers add up to k
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
Bonus: can you do this in one pass?
'''

def add_to_k(list, k):
    for i in range(len(list)):
        for j in range(1, len(list) - i):
            if (list[i] + list[i+j] == k):
                print True
            else:
                print False



print (add_to_k([10, 15, 3, 7], 17))
