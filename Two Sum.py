class Solution:
    def twoSum(self, nums, target):
        data = dict()
        for i in range(len(nums)):
            if nums[i] in data:
                data[nums[i]].append(i)
            else:
                data[nums[i]] = [i]
        for i in nums:
            if target == 2 * i and len(data[i]) > 1:
                return [data[i][0], data[i][1]]
            elif (target - i) in data and target != 2 * i:
                return [data[i][0], data[target - i][0]]
