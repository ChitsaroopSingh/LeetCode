class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sum1=0
        sum2=0
        for i in range(0,n,2):
            sum1+=nums[i]
        for i in range(1,n,2):
            sum2+=nums[i]
        return sum1-sum2
        
        