class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m_idx = m - 1
        n_idx = n - 1
        right = n + m - 1
        while n_idx >= 0:
            if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
                nums1[right] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[right] = nums2[n_idx]
                n_idx -= 1

            right -= 1