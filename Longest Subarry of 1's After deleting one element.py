nums = list(map(int, input().split()))
n = len(nums)

left = 0
zeros = 0
ans = 0
for right in range(n):
    if nums[right] == 0:
        zeros += 1
    while zeros > 1:
        if nums[left] == 0:
            zeros -= 1
        left += 1
    ans = max(ans, right - left + 1 - zeros)
print(ans - 1 if ans == n else ans)


