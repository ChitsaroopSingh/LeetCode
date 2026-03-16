class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text=text.lower()
        text=text.split()

        text.sort(key=len)
        text[0] = text[0].capitalize()
        return ' '.join(text)
        