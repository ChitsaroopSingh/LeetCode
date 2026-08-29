class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """

        op = []
        j = 0
        for i in range(1, n + 1):           
            op.append("Push")
            if i == target[j]:
                j += 1                
                if j == len(target):
                    break
            else:
                op.append("Pop")
        return op

                
            

        