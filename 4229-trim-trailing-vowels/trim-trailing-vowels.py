class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=list(s)
        for i in range(len(x)-1,-1,-1):
            if x[i] in 'aeiou':
                x.pop(i)
            else:
                break
        return "".join(x)