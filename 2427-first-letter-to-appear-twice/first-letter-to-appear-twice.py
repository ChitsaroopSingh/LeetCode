class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=set()
        for ch in s:
            if ch not in a:
                a.add(ch)
            else:
                return ch
        