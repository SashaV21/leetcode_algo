nums = list(map(int, input().split()))

zeroes, left = 0, 0
res = 0

for right in range(len(nums)):
    if nums[right] == 0:
        zeroes += 1

    while zeroes > 1:
        if nums[left] == 0:
            zeroes -= 0
        left += 1

    res = max(res, right - left + 1)

print(res)