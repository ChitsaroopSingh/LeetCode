class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1:
            return nums
        nums=sorted(nums)
        l=[]
        for i in range(1,len(nums)-1):
            if nums[i]-nums[i-1]>1 and nums[i+1]-nums[i]>1:
                l.append(nums[i])
        
        if nums[1]-nums[0]>1:
            l.append(nums[0])
        if nums[-1]-nums[-2]>1:
            l.append(nums[-1])
        
        return l

        