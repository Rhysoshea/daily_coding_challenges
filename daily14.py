'''
The area of a circle is defined as pi.r^2. Estimate pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

circle inside a square
        2r
   1|--ooooooo--|
    | ooooooooo |
    |ooooooooooo|  2r
    | ooooooooo |
  -1|__ooooooo__|
    -1          1

area of circle pir^2
area of square 4r^2

ratio of circle to square = pir^2 / 4r^2 = pi/4

randomly sample points in this square and count how many fall in the circle
this will give another ratio
'''

from random import uniform
import math

def generate():
    return (uniform(-1,1), uniform(-1,1))

def is_in_circle(coords):
    # checks x^2 + y^2 is inside the bounds of r^2
    return coords[0]*coords[0] + coords[1]*coords[1] < 1

def monte_carlo(iterations):
    count = 0
    for _ in range(iterations):
        if is_in_circle(generate()):
            count += 1
    pi = (count/iterations)*4
    return pi

# extension of problem to check accuracy of estimate
def check_pi(iterations):
    pi_range = []
    for _ in range(iterations):
        pi_range.append(monte_carlo(iterations))

    return pi_range

# print ("{0:.3f}".format(monte_carlo(1000)))
arr = check_pi(1000)
print ("Mean: {0:.3f}".format(sum(arr)/len(arr)))
print ("Min: {0:.3f}".format(min(arr)))
print ("Max: {0:.3f}".format(max(arr)))
