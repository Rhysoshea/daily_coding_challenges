"""
https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms


return the maximum luck possible from losing no more than k important competitions
important = 1
unimportant = 0
gain luck by losing competitions
want to sort by important competitions and amount of luck
"""

def solution(k, contests):
    unimportant = [x for x in contests if not x[1]]
    important = [x for x in contests if x[1]]
    luck = sum([x[0] for x in unimportant])

    important = sorted(important, key = lambda x: (x[1], x[0]), reverse=True)
    
    luck += sum([x[0] for x in important[:k]])
    luck += sum([-x[0] for x in important[k:]])

    return luck
    
k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

assert (solution(k, contests) == 29)