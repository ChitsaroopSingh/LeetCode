class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ki=k
        t=0
        while t<=len(nums):
            if k in nums:
                k+=ki
            else:
                return k
                break
            t+=1

        
        