class Solution(object):
    def isSubsequence(self, s, t):
        s_p, t_p = 0, 0
        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t_p:
                s_p += 1
            t_p += 1

        return len(s) == s_p