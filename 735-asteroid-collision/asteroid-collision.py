class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(asteroids)
        for i in range(n):
            cur = asteroids[i]
            alive = True
            while alive and stack and stack[-1] > 0 and cur < 0:                
                if abs(stack[-1])<abs(cur):
                    stack.pop()
                elif abs(stack[-1]) == abs(cur):
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(cur)
        return stack
            
        