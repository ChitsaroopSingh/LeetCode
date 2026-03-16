class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if max(nums)<=5:
        #     return 0
        def f(n):
            count=0
            total=0
            for i in range(1,int(n**0.5)+1):
                if n%i==0:
                    j=n//i
                    if i==j:
                        count+=1
                        total+=i
                    else:
                        count+=2
                        total+=i+j
                    if count>4:
                        return 0
            return total if count==4 else 0
        ans=0
        for num in nums:
            ans+=f(num)
        return ans




        