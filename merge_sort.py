class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a=n
        for i in range(a):
            nums1[m+i]=nums2[a-1]
            while a<0:
                return
            a-=1
        nums1.sort()
