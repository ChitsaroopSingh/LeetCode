class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        newset=set(candyType)
        s=len(newset)
        n=len(candyType)//2
        
        return min(s,n)
        