# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

def solution(arr):
    

    maximum = 0
    first = arr[0]
    buys = [first]

    i = 1

    while i < len(arr):
        price = arr[i]
        for buy in buys:
            if price-buy > maximum:
                maximum = arr[i]-buy 

        buys.append(arr[i])
        i += 1

    return maximum

def solutionTwo(arr):

    maxPrice = 0
    maxDiff = 0
    arr.reverse()

    for price in arr:
        if price > maxPrice:
            maxPrice = price 
        if maxPrice - price > maxDiff:
            maxDiff = maxPrice - price 

    return maxDiff

print (solution([9,11,8,5,7,10]))
print (solution([9,8,7,6,5,4,3,2,1]))
print (solutionTwo([9,11,8,5,7,10]))
print (solutionTwo([9,8,7,6,5,4,3,2,1]))