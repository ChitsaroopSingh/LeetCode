class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=str(abs(n))
        x = [int(d) for d in num]
        a=max(x)
        x.remove(a)

        return a*max(x)
        