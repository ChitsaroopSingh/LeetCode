class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a=set(nums1)
        b=set(nums2)
        c=a.intersection(b)
        x=list(c)
        if len(x)==0:
            return -1
        return min(x)
        