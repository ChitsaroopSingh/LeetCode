class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=1
        s=set(nums)
        while i<len(nums):
            if i not in s:
                return False
                break
            i+=1
        n=len(nums)-1
        if max(nums)==n and nums.count(n)==2:
            return True
        else:
            return False
        