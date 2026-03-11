class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """

        count=[0]*60
        pairs=0

        for x in time:
            r=x%60
            need=(60-r)%60
            pairs+=count[need]
            count[r]+=1
        return pairs