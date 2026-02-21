class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lsum=0
        ls=[0]*len(nums)
        rsum=0
        rs=[0]*len(nums)
        for i in range(len(nums)):
            ls[i]=lsum
            lsum+=nums[i]
        for i in range(len(nums)-1,-1,-1):
            rs[i]=rsum
            rsum+=nums[i]
        
        answer=[0]*len(nums)
        for i in range(len(nums)):
            answer[i]=abs(ls[i]-rs[i])
        return answer
