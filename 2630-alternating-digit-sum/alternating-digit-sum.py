class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=0
        d = [int(x) for x in str(n)]
        for i in range(len(d)):
            if i%2==0:
                s+=d[i]
            else:
                s-=d[i]
        return s
        