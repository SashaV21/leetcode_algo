class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        len_s, len_t = len(s), len(t)
        if len_s - len_t > 1:
            return False
        for idx in range(len_t):
            if s[idx] != t[idx]:
                if len_s == len_t:
                    return s[idx + 1:] == t[idx + 1:]
                else:
                    return s[idx + 1:] == t[idx:]
        return len_s == len_t + 1
