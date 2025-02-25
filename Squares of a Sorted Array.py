class Solution(object):
    def sortedSquares(self, nums):
        res = [0] * len(nums)
        right = len(nums) - 1
        left = 0
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1
            else:
                res[i] = nums[right] ** 2
                right -= 1

        return res