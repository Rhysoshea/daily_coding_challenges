'''
For a 6x6 array, calculate the maximum hourglass sum where an hourglass is:

a b c
  d
e f g

'''

def hourglassSum(arr):
    ans = 0
    for x in range(int(len(arr)/2)+1):
        for y in range(int(len(arr[x])/2)+1):
            sum_nums = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            ans = max(ans,sum_nums)
    return ans

array = [[1, 1, 1, 0, 0, 0],
          [0, 1, 10, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]
assert hourglassSum(array) == 20
