class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack=[]

        for char in s:
            stack.append(char)
            if ''.join(stack[-len(part):]) == part:
                for i in range(len(part)):
                    stack.pop() 
        return ''.join(stack)
        