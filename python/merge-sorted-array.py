class Solution(object):
    def merge(self, nums1, m, nums2, n):
        length = m + n
        index = 0

        for i in range(length - n, length):
            nums1[i] = nums2[index]
            index += 1

        nums1.sort()