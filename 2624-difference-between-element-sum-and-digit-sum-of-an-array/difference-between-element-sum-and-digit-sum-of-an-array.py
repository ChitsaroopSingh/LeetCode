class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele=sum(nums)
        result=[]
        for n in nums:
            if n >= 10:
                result.extend([int(d) for d in str(n)])
            else:
                result.append(n)
        s=sum(result)
        return abs(ele-s)


        