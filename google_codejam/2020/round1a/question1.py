'''
question1

'''

def solution(input):
    input = list(set(input))
    input = sorted(input, key=len ,reverse=True)
    print(input)
    exit()
    arr = []
    arr.append([char for char in input[0]])
    input.pop(0)

    for word in input:
        for char in word:
            if char=="*":
                

                print(char)
        print('\n')
    return '*'

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(input())
        # print(arr)
        ans = solution(arr)
        print("Case #{}: {}".format(i+1, ans))
