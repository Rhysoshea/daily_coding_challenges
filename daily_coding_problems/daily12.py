'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

1 step
[1]

2 steps
[1,1]
[2]

For example, if N is 3, then there are 3 unique ways:

[1, 1, 1]
[2, 1]
[1, 2]

For example, if N is 4, then there are 5 unique ways:

[1, 1, 1, 1]
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
[2, 2]

5 steps = 8 ways

f(N) = f(N-1) + f(N-2) is the Fibonacci sequence

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

Generalising to any number of steps in say X = {1, 3, 5}
f(N) = f(N-1) + f(N-3) + f(N-5)
'''
# simplifies to the fibonacci sequence
def staircase_fib(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
        print (a, b)
    return a
print (staircase_fib(4))
'''
def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return sum(staircase(n - x, X) for x in X)
'''

# This is again, very slow (O(|X|**N)) since we are repeating computations again. We can use dynamic programming to speed it up.

# Each entry cache[i] will contain the number of ways we can get to step i with the set X. Then, we'll build up the array from zero using the same recurrence as before:

# def staircase(n, X):
#     cache = [0 for _ in range(n + 1)]
#     cache[0] = 1
#     for i in range(1, n + 1):
#         cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
#     return cache[n]
# This now takes O(N * |X|) time and O(N) space.


# print (staircase_(10, {1,2,5}))
