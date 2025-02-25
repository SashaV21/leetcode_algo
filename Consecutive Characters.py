s = input()

prev_val = s[0]
count = 1
res = 0
for i in range(1, len(s)):
    if s[i] == prev_val:
        count += 1
    else:

        count = 1
    res = max(count, res)
    prev_val = s[i]

print(res)