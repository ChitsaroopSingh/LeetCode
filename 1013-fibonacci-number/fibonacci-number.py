class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def seq(x):
            if x<=1:
                return x
            else:
                return seq(x-1)+seq(x-2)
        return seq(n)
        
        