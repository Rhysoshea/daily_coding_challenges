"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
def encode(code):
    output = ""
    i = 0
    while True:
        if i >= len(code)-1:
            break
        count = 1
        letter = code[i]
        while i+1 < len(code) and letter == code[i+1] :
            count += 1
            i += 1
        i += 1
        output += f'{count}{letter}'
    return output

def decode(code):
    output = ""

    for i in range(0,len(code)-1,2):
        output += int(code[i])*code[i+1]

    return output

def test1(input, ans):
    assert (encode(input) == ans)
def test2(input, ans):
    assert (decode(input) == ans)

code1 = "AAAABBBCCDAA"
code2 = "4A3B2C1D2A"


test1(code1, code2)
test2(code2, code1)
