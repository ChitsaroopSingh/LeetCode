class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            x=min(nums)
            y=nums.index(x)
            nums[y]=-nums[y]
        return sum(nums)
        