class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        word=list(word)
        for i in range(len(word)):
            if ord(word[i])>=97 and ord(word[i])<=122:
                word[i]= " "
        x=''.join(word)
        x=x.lstrip()
        x=x.split()
        y=[i.lstrip('0') for i in x]

        return len(set(y))