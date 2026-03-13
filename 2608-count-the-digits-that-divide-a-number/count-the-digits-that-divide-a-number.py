class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=[]
        numc=num
        while numc>0:
            d=numc%10
            if num%d==0:
                count.append(d)
            numc//=10
        return len(count)