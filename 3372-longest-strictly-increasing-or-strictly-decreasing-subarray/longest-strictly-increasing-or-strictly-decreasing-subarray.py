class Solution(object):
    def longestMonotonicSubarray(self, nums):
        if not nums:
            return 0

        count=[]
        c=1
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
            else:
                count.append(c)
                c=1
        count.append(c)
        c=1  
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                c+=1
            else:
                count.append(c)
                c=1
        count.append(c)
        return max(count)