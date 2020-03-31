'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

class Trie(object):
    def __init__(self):
        self.trie = {}

    def insert(self, text):
        trie = self.trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie["$"] = True

    def elements(self, prefix):
        t = self.trie
        for char in prefix:
            if char in t:
                t = t[char]
            else:
                return []
        return self._elements(t)

    def _elements(self, t):
        result = []
        for c, v in t.items():
            if c == "$":
                subresult = ['']
            else:
                subresult = [c+s for s in self._elements(v)]
            result.extend(subresult)
        return result

    def _print(self, trie):
        print (self.trie.items())

def autocomplete(s):
    print ([s + w for w in trie.elements(s)])

s = 'destruct'
set_strings = ['destruction', 'destruct', 'hello', 'assfjkls']

trie = Trie()
for text in set_strings:
    trie.insert(text)

# trie._print(trie)
autocomplete(s)
