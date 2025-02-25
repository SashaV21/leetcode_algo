class Solution(object):
    def firstUniqChar(self, s):
        book = dict()
        for i in range(len(s)):
            book[s[i]] = 1 + book.get(s[i], 0)

        for i, ch in enumerate(s):
            if book[ch] == 1:
                return i
        return -1


