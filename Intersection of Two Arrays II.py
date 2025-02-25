
class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        book = dict()
        for num in nums1:
            book[num] = 1 + book.get(num, 0)

        res  = []

        for num in nums2:
            if num in book and book[num] > 0:
                res.append(num)
                book[num] -= 1

        return res

