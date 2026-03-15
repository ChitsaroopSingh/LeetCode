class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>=1000:
            return n-1000+1
        return 0
        