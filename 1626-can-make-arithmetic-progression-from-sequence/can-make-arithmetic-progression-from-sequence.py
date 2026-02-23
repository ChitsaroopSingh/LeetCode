class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ans=sorted(arr)
        d=ans[1]-ans[0]
        count=0
        for i in range(1,len(ans)):
            if ans[i]-ans[i-1]==d:
                count+=1
            else:
                count+=0
        if len(ans)-1==count:
            return True
        else:
            return False
        