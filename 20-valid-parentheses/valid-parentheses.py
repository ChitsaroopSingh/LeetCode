class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for brac in s:
            if brac == "(" or brac == "[" or brac == "{":
                stack.append(brac)
            else:
                if len(stack) == 0:
                    return False
                elif brac == ")" and stack[-1] == "(":
                    stack.pop()

                elif brac == "]" and stack[-1] == "[":
                    stack.pop()

                elif brac == "}" and stack[-1] == "{":
                    stack.pop()

                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        