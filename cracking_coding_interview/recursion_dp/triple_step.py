# there are n steps, can take 1,2 or 3 steps at a time
# how many different ways are there to get up the steps


def staircase(n, X):

    cache = [0 for x in range(n+1)]
    cache[0] = 1

    for i in range(len(cache)):
        for x in X:
            if i-x >= 0:
                cache[i] +=  cache[i-x]

    return(cache[-1])

print (staircase(10, [1,2,3]))