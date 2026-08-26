class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for char in operations:
            if char != "C" and char != "D" and char != "+":
                num = int(char)
                stack.append(num)
            elif char == "C":
                stack.pop()
            elif char == "D":
                stack.append(2*stack[-1])
            elif char == "+":
                stack.append(stack[-1]+stack[-2])
        return (sum(stack))