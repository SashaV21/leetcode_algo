data = list(map(int, input().split()))

max_pos = 0
for i in range(len(data)):
    if data[i] > data[max_pos]:
        max_pos = i

ans = 0
nowm = 0

for i in range(max_pos):
    if data[i] > nowm:
        nowm = data[i]
    ans += nowm - data[i]

nowm = 0

for i in range(len(data) - 1, max_pos, -1):
    if data[i] > nowm:
        nowm = data[i]
    ans += nowm - data[i]

print(ans)