class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        n = len(nums)

        for i in range(n):
            ans.append(nums[i])

        for i in range(n):
            ans.append(nums[i])

        return ans