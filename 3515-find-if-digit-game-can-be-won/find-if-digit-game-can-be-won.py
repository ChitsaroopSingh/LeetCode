class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        g=0
        l=0
        for i in range(len(nums)):
            if nums[i]>=10:
                g+=nums[i]
            else:
                l+=nums[i]
        if g==l:
            return False
        else:
            return True


        