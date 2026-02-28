class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=int(s,2)
        count=0
        while x!=1:
            if x%2==0:
                x/=2
                count+=1
            else:
                x+=1
                count+=1
        return count
        