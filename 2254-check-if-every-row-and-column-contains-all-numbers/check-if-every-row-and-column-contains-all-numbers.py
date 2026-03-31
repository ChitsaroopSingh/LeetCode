class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n=len(matrix)
        esum= n*(n+1)/2

        for row in matrix:
            if sum(row)!=esum or len(set(row))!=n:
                return False
        for col in range(n):
            cval=[matrix[row][col] for row in range(n)]
            if sum(cval)!=esum or len(set(cval))!=n:
                return False
        return True
        