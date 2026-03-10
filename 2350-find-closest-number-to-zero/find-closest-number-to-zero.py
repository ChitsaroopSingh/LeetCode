class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[i**2 for i in nums]
    
        t=int((min(num))**0.5)
        if t in nums:
            return t
        else:
            return -t


        