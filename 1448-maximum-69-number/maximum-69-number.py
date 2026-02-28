class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        d=[int(digit) for digit in str(num)]
        print(d)
        for i in range(len(d)):
    
            if d[i]==6:
                d[i]=9
                break

        return int("".join(map(str,d)))
        