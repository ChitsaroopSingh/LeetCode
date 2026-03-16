class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a=max(candies)
        result=[]
        c=[i+extraCandies for i in candies]
        for i in range(len(candies)):
            if c[i]>=a:
                result.append(True)
            else:
                result.append(False)
        return result
        