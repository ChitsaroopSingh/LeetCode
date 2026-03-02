class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=[abs(i) for i in nums]

        nums=sorted(t,reverse=True)
        arr=[0]*len(nums)
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            if i%2==0:
                arr[i]=nums[l]
                l+=1
            else:
                arr[i]=nums[r]
                r-=1

        s = [i*i for i in arr]
        score=0
        for i in range(len(s)):
            if i%2==0:
                score+=s[i]
            else:
                score-=s[i]
        return score

        