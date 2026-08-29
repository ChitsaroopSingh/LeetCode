class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        stack = []
        count = 0
        for d in directions:
            if d == "R":
                stack.append("R")              
            elif d == "S":
                while stack and stack[-1] == "R":
                    count += 1
                    stack.pop()
                stack.append("S")               
            elif d == "L":
                if stack:
                    if stack[-1] == "R":
                        count += 2
                        stack.pop()
                        while stack and stack[-1] == "R":
                            count += 1
                            stack.pop()
                        stack.append("S") 
                    elif stack[-1] == "S":
                        count += 1
                        stack.append("S")
        return count

      