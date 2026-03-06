class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        # ci=1
        for i in range(n):
            while nums[i]>=1 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                ci=nums[i]-1
                nums[i],nums[ci]=nums[ci],nums[i]
                # nums[ci]=nums[i]
        # print(nums)
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
    
        