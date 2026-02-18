class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        x=list(command)
        a = [ord(c) for c in x]
        abc=[]

        for i in range(len(a)):
            if a[i]==71:
                abc.append(chr(a[i]))
            if a[i]==40 and a[i+1]==41:
                abc.append("o")
            if a[i]==97 and a[i+1]==108:
                abc.append("al")
            
        result = ''.join(abc) 

        return result

        
        