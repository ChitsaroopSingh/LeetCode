class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(str(n).replace('0',''))