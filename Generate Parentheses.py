def dfs(res, open, close, s):
    if open == close and open + close == 2 * n:
        res.append(s)
        return

    if open < n:
        dfs(res, open + 1, close, s + '(')

    if close < open:
        dfs(res, open, close + 1, s + ')')


n = int(input())
res = []
dfs(res, 0, 0, '')
print(res)


