def find_short(s):
    # your code here
    arr = s.split(' ')
    l = min([len(x) for x in arr])
    return l # l: shortest word length

assert find_short("bitcoin take over the world maybe who knows perhaps") == 3
