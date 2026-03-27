class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=[]
        for ch in s:
            if ch=="i":
                r.reverse()
            else:
                r.append(ch)
        return "".join(r)


        