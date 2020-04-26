# https: // codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

# Problem
# You have just received the best gift ever: an Expogo stick. You can stand on it and use it to make increasingly large jumps.

# You are currently standing on point(0, 0) in your infinite two-dimensional backyard, and you are trying to reach a goal point(X, Y), with integer coordinates, in as few jumps as possible. You must land exactly on the goal point
# it is not sufficient to pass over it on a jump.

# Each time you use your Expogo stick to jump, you pick a cardinal direction: north, south, east, or west. The i-th jump with your Expogo stick moves you 2(i-1) units in the chosen direction, so your first jump takes you 1 unit, your second jump takes you 2 units, your third jump takes you 4 units, and so on.

# Given a goal point(X, Y), determine whether it is possible to get there, and if so, demonstrate how to do it using as few jumps as possible.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow. Each consists of a single line with two integers X and Y: the coordinates of the goal point.

# Output
# # x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if the goal point cannot be reached. Otherwise, y must be a string of one or more characters, each of which is either N (north), S (south), E (east), or W (west), representing the directions of the jumps that you will make, in order. This sequence of jumps must reach the goal point at the end of the final jump, and it must be as short as possible.
# For each test case, output one line containing Case

# Limits
# Time limit: 20 seconds per test set.
# Memory limit: 1GB.
# (X, Y) ≠ (0, 0).

# Test set 1 (Visible Verdict)
# 1 ≤ T ≤ 80.
# -4 ≤ X ≤ 4.
# -4 ≤ Y ≤ 4.

# Test set 2 (Visible Verdict)
# 1 ≤ T ≤ 100.
# -100 ≤ X ≤ 100.
# -100 ≤ Y ≤ 100.

# Test set 3 (Visible Verdict)
# 1 ≤ T ≤ 100.
# -109 ≤ X ≤ 109.
# -109 ≤ Y ≤ 109.

    

def solution(x,y):
    if (abs(x) + abs(y))%2 == 0:
        return "IMPOSSIBLE"
    
    ans = ""

    while x != 0 or y != 0:
        if abs(x) == 1 and y == 0:
            if x > 0:
                ans += "E"
                break 
            else:
                ans += "W"
                break
        if x == 0 and abs(y) == 1:
            if y > 0:
                ans += "N"
                break
            else:
                ans += "S"
                break
        if x%2!=0:
            if (abs(x+1)/2 + abs(y)/2) % 2 != 0:
                x = (x+1)/2
                y = y/2
                ans += "W"
            else:
                x = (x-1)/2
                y = y/2
                ans += "E"

        elif y%2!=0:
            if (abs(x/2) + abs(y+1)/2)%2 != 0:
                y = (y+1)/2
                x = x/2
                ans += "S"
            else:
                y = (y-1)/2
                x = x/2
                ans += "N"

        else:
            return "IMPOSSIBLE"


    return ans


if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        # n = number of bits
        # b = number of broken workers
        # f = number of attempts
        x, y = input().strip().split()
        ans = solution(int(x), int(y))
        print("Case #{}: {}".format(i+1, ans))
