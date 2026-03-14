class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        vol=length*width*height
        if length>=10000 or width>=10000 or height>=10000 or vol>=10**9:
            bulky=True
        else:
            bulky=False
        if mass>=100:
            heavy=True
        else:
            heavy=False
        if bulky==True and heavy==True:
            return "Both"
        elif bulky==False and heavy==False:
            return "Neither"
        elif bulky==True and heavy==False:
            return "Bulky"
        else:
            return "Heavy"
        