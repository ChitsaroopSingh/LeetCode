class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ascii_values = [ord(c) for c in s]
        score=0
        for i in range(1,len(ascii_values)):
            score+=abs(ascii_values[i]-ascii_values[i-1])
        return score

        