class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b=set(nums)
        s=min(nums)
        l=max(nums)
        arr=[]
        for i in range(s,l+1):
            arr.append(i)

        c=set(arr)
        return sorted(list(c-b)) 
