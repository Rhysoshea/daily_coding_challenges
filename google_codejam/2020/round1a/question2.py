'''
question2

'''

def solution(input):
    # first to find out how large a Pascal triangle we will need
    n = 0
    total = 0
    while total < input:
        n+=1
        total = (2**n)-1

    binary = int(bin(input).split('b')[1])
    n=0
    positions=[]
    total = 0
    rows = []
    reverse = False
    while binary > 0:
        n+=1
        rem = binary%10
        binary = binary//10
        # print(reverse)
        if rem == 1:
            rows.append(n)
            if reverse:
                positions.extend([[n, x+1] for x in range(n)[::-1]])
            else:
                positions.extend([[n,x+1] for x in range(n)])
            total+= 2**(n-1)
            reverse = not reverse
        elif reverse:
            positions.extend([[n, n]])
            total+=1
        else:
            positions.extend([[n, 1]])
            total += 1

    # need to alternate the direction for each row
    # print(positions)
    # print(rows)
    # print(total)
    while total > input:
        while n not in rows:
            n-=1
        if [n,n] in positions:
            positions.pop(positions.index([n,n]))
            total-=1
        elif [n, 1] in positions:
            positions.pop(positions.index([n, 1]))
            total-=1
        else:
            n-=1

    # print(positions)
    # print(total)
    return positions

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        ans = solution(n)
        print("Case #{}:".format(i+1))
        for tuple in ans:
            print("{} {}".format(tuple[0], tuple[1]))
