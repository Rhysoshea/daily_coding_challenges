"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

        30----------------75
0--------------50
                    60------------------------150
"""

def solution(input):
    #O(N^2) time due to running through every class row every time N*N
    counter_per_class = [1]*len(input)

    for i,time in enumerate(input):
        count1 = 1
        count2 = 1
        for j in range(0,len(input)):
            if j!=i:
                # print (f'time1 {time}  time2  {input[j]}')
                if time[0] > input[j][0] and time[0] < input[j][1]:
                    count1 += 1
                if time[1] > input[j][0] and time[1] < input[j][1]:
                    count2 += 1
                # print (f'count1 {count1} count2 {count2}')
                counter_per_class[j] = max(counter_per_class[j],max(count1,count2))
    # print (counter_per_class)

    return max(counter_per_class)

"""
        30----------------75
0--------------50
                    60------------------------150

0  30  60
50 75  150

"""
def solution2(input):
    #runs in O(NlogN) due to sorting taking logN time then running through by N
    starts = sorted(start for start,end in input)
    ends = sorted(end for start,end in input)
    print

    i,j = 0,0
    current_overlap = 0
    current_max = 0

    while i<len(input) and j<len(input):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i +=1
        else:
            current_overlap -= 1
            j +=1
    return current_max

def test(input, ans):
    assert (solution2(input) == ans)


input1 = [(30, 75), (0, 50), (60, 150)]
input2 = [(30, 75), (0, 50)]
input3 = [(30, 75), (0, 50), (60, 150), (50,60)]
input4 = [(30, 75), (0, 50), (60, 150), (0,150)]
input5 = [(30, 75), (0, 65), (60, 150)]


print (solution2(input1))

test(input1, 2)
test(input2, 2)
test(input3, 2)
test(input4, 3)
test(input5, 3)
