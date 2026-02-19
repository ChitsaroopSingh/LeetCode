class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        nums=sorted(piles)
        n=len(piles)/3
        coins=0

        for i in range(n,3*n,2):
            coins+=nums[i]
        return coins

        