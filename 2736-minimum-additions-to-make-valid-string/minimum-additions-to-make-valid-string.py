class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        word=word.replace('abc','0 ')
        word=word.replace('ab','1 ')
        word=word.replace('bc','1 ')
        word=word.replace('ac','1 ')
        word=word.replace('a','2 ')
        word=word.replace('b','2 ')
        word=word.replace('c','2 ')
        word=word.split()
        x=[int(i) for i in word]
        return sum(x)