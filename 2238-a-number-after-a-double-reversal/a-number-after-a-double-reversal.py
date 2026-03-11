class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x=str(num)
        t=x[::-1]
        s = t.lstrip('0')    
        if s=='': #edgecase
            s='0'   
        z=s[::-1]
        y=int(z)
        if y==num:
            return True
        else:
            return False
        
        