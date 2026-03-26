class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        x=s.count(letter)
        l=len(s)
        return int((x*100)/l)
        