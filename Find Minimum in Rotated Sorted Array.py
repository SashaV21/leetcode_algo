def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        midl = (left + right) // 2
        if nums[midl] <= nums[right]:
            right = midl
        else:
            left = midl + 1

    return nums[left]


def main():
    print(findMin([3,4,5,1,2]))
    print(findMin([4,5,6,7,0,1,2]))
    print(findMin([11,13,15,17]))
    print(findMin([1,2]))

if __name__ == '__main__':
    main()