'''
Order an array of numbers by their weight
The weight of a number is the sum of its digits
'''

def order_weight(strng):
    if strng === '':
        return (strng)
    arr = strng.split(' ')
    # print (arr)
    weights = []
    for i in arr:
        s = 0
        for j in i:
            s += int(j)
        weights.append(s)

    # print (weights)
    # s = weights.sort()
    # print (s)

    while (weights != weights.sort()):
        sort_func(weights, arr)
    result = ' '.join(str(x) for x in arr)
    print (result)

def sort_func(weights, arr):
    for i in range(len(weights)-1):
        # print (weights[i+1])
        if (weights[i] > weights[i+1]):
            # print (weights[i])
            temp_w = weights[i]
            weights[i] = weights[i+1]
            weights[i+1] = temp_w

            temp_a = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp_a

            return (weights, arr)

        elif (weights[i] == weights[i+1]):
            # print (weights[i])
            num1 = [int(d) for d in str(arr[i])]
            num2 = [int(d) for d in str(arr[i+1])]
            # print (num1[0])
            # print (num2[0])
            if (num1[0]) > (num2[0]):
                temp_w = weights[i]
                weights[i] = weights[i+1]
                weights[i+1] = temp_w

                temp_a = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp_a
                # print (weights)
                return (weights, arr)

order_weight("56 65 74 100")

    # sorted = []
    # sort_weight = []
    # for i in weights:
    #     if not sorted:
    #         sorted.append(arr[i])
    #         sort_weight.append(weight[i])
    #     else:
    #         for

# order_weight("56 65 74 100 99 68 86 180 90")


    # map = dict(zip(arr, weights))
    # weights.sort()
    # result = []
    # print (map)
    # print (weights)
    # for x in weights:
    #     print (x)
    #     result.append(map[x])
    # str1 = ' '.join(str(x) for x in result)
    # print (str1)
