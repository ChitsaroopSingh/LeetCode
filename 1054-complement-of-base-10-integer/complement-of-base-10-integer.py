class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        b = bin(n)[2:]


        complement = ""
        for bit in b:
            if bit == "1":
                complement += "0"
            else:
                complement += "1"



        return int(complement,2)
