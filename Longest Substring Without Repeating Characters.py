from leetcod3 import length


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        book = {}
        l = 0
        length = 0
        for r in range(len(s)):
            symbol = s[r]
            if symbol in book and book[symbol] >= l:
                l = book[symbol] + 1
            else:
                length = max(length, r - l + 1)
            book[symbol] = r

        return length