class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        b = bin(num)[2:]
        complement = ""
        for bit in b:
            if bit == "1":
                complement += "0"
            else:
                complement += "1"
        return int(complement,2)

        