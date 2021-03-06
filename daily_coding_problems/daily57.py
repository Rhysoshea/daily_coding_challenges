# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.

# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


def breakText(text, k):

    words = text.split()
    if not words:
        return []
    output = []
    i = 0
    current = ""
    while i < len(words):
        if current == "":
            if len(words[i]) > k:
                return None
            else:
                current += words[i] 
                i+=1
        else:
            if len(current + " " + words[i]) <= k:
                current += " " + words[i]
                i+=1
            else:
                output.append(current)
                current = ""
        if i == len(words) and current:
            output.append(current)

    return output





print (breakText("the quick brown fox jumps over the lazy dog",10))
print (breakText("the quick brown fox jumps over the lazy dog",5))
print (breakText("the quick brown fox jumps over the lazy dog",4))
print (breakText("the quick brown fox jumps over the lazy dog",20))