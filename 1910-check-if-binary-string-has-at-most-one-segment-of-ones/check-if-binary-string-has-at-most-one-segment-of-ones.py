class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.strip('0')
        if s.count('1')==len(s):
            return True

        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                return False
            
        