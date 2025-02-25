s = input()

s = s[::-1]

s = list(s.split(' '))

res = []
for i in range(len(s) - 1, -1, -1):
    res.append(s[i])
print(' '.join(res))


