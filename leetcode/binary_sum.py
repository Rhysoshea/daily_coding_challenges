"""
Given 2 strings in binary add both numbers together and return their binary sum
"""
# 110011
#   1010
# 111101  ans

#    11010, 
# 00101001
#  1000011  ans

line = "110011,1010"
    
num1, num2 = line.split(',')
i = len(num1)
j = len(num2)

ans = ""
carry = 0

# buffer with zeroes
if i != j:
    if i < j:
        num1 = num1.zfill(j)
    else:
        num2 = num2.zfill(i)

for i in reversed(range(len(num1))):

    if num1[i] != num2[i]: # 1 and 0
        if carry > 0:
            ans += "0"
            carry -= 1 
        else:
            ans += "1"

    else:
        if num1[i] == "1": # 1 and 1
            if carry > 0:
                ans += "1"
                carry -= 1
            else:
                ans += "0"
                carry += 1
        else: # 0 and 0
            if carry > 0:
                ans += "1"
                carry -= 1
            else:
                ans += "0"

print(str(int(ans[::-1])), end="\n") #drop leading zeroes
