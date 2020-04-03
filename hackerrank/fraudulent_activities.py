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

def insertSort(arr, new):
    arr.pop(0)
    arr.append(new)
    i = len(arr)-1
    while arr[i] > new and i>=0:
        arr[i+1] = arr[i]
        i -= 1
    arr[i] = new

    return arr

def fraudulentSpend(n, d, arr):
    count = 0
    if len(arr) < 2:
        return 0
    # sortedArr = sorted(arr[0:d])
    # print(sortedArr)
    for i in range(n-d):
        if i == 0:
            sortedArr = sorted(arr[0:d])
        else:
            sortedArr = insertSort(sortedArr,arr[i+d-1])
        print(sortedArr)
        print(arr[i+d], returnMedian(sortedArr))
        if arr[i+d] >= 2*(returnMedian(sortedArr)):
            count += 1
    print (count)
    return count


# def fraudulentSpend(n, d, arr):
#     count = 0
#     if d % 2 == 0:
#         for i in range(n-d):
#             median = (arr[i+(d//2)]+arr[i+(d//2)-1])/2
#             if arr[i+d] >= 2*median:
#                 count += 1
#     else:
#         for i in range(n-d):
#             median = arr[i+(d//2)]
#             if arr[i+d] >= 2*median:
#                 count += 1
#     print(count)
#     return count

assert (fraudulentSpend(9, 1, [2, 3, 4, 2, 3, 6, 8, 4, 5])==2)
# assert (fraudulentSpend(5, 4, [1, 2, 3, 4, 4]) == 0)
# assert (fraudulentSpend(5, 1, [10, 20, 30, 40, 50]) == 1)
