class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        digits = []
        for num in nums:
            for d in str(num):
                digits.append(int(d))
        return digits
        