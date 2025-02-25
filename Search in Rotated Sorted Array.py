def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def main():
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
    print(search([1], 0))


if __name__ == '__main__':
    main()
