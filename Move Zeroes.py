nums = list(map(int, input().split()))

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[right], nums[left] = nums[left], nums[right]
        left += 1
print(nums)