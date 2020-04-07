"""
Fraudulent activities
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""

def returnMedian(arr):
    n = len(arr)
    # print(arr)
    if n%2 == 0:
        return (arr[n//2]+arr[(n//2)-1])/2
    return arr[n//2]

# use insert sort to speed up, still not fast enough
def insertSort(arr, new):
    arr[0] = new
    i = 0
    if len(arr) < 2:
        return arr
    while arr[i+1] < new:
        arr[i] = arr[i+1]
        i += 1
        if i >= len(arr)-2:
            break
        # print(i)
    arr[i] = new
    return arr

# use count sort to speed up further still
# def countSort(arr):
#     counts = [0]*(max(arr)+1)
#     for i in arr:
#         counts[i] += 1
#     output = []

#     for i, count in enumerate(counts):
#         output.extend([i]*count)
#     return output


def countSort(arr):
    output = []
    for i, count in enumerate(arr):
        output.extend([i]*count)
    return output

def fraudulentSpend(n, d, arr):
    count = 0
    if len(arr) < 2:
        return 0
    historic_count = [0] * (max(arr)+1)
    for i in range(len(arr)-1):
        historic_count[arr[i]] += 1
        sortedArr = countSort(historic_count)
        if i+1 >= d:
            # print(sortedArr)
            # print(returnMedian(sortedArr))
            if arr[i+1] >= 2*(returnMedian(sortedArr)):
                count += 1
            historic_count[sortedArr[0]] -= 1

    # print (count)
    return count


assert (fraudulentSpend(9, 1, [2, 3, 4, 2, 3, 6, 8, 4, 5])==1)
assert (fraudulentSpend(5, 4, [1, 2, 3, 4, 4]) == 0)
assert (fraudulentSpend(5, 3, [10, 20, 30, 40, 50]) == 1)

