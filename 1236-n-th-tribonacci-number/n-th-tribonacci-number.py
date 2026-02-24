class Solution(object):
    def tribonacci(self, n):
        memo = {}
        def tb(n):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            if n==2:
                return 1
            memo[n] = tb(n-1)+tb(n-2)+tb(n-3)
            return memo[n]
        return tb(n)