nums = list(map(int, input().split()))
k = int(input())

l = 0
zeroes = 0
res = 0

for r in range(len(nums)):
    if nums[r] == 0:
        zeroes += 1

    while zeroes > k:
        if nums[l] == 0:
            zeroes -= 1
        l += 1

    res = max(res, r - l + 1)

print(res)


