class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        n=len(stockPrices)
        if n==1:
            return 0
        stockPrices.sort()

        lines=1

        dyi=stockPrices[1][1]-stockPrices[0][1]
        dxi=stockPrices[1][0]-stockPrices[0][0]

        for i in range(2,n):
            dy=stockPrices[i][1]-stockPrices[i-1][1]
            dx=stockPrices[i][0]-stockPrices[i-1][0]

            if dy*dxi != dx*dyi:
                lines+=1

                dyi=dy
                dxi=dx
        return lines

