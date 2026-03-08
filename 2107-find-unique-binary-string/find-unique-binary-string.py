class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        r=''
        for i in range(len(nums)):
            if nums[i][i]=='0':
                r+='1'
            else:
                r+='0'

        return r

        