class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        
        count=[0]*24
        pairs=0

        for x in hours:
            r=x%24
            need=(24-r)%24
            pairs+=count[need]
            count[r]+=1

        return pairs
        