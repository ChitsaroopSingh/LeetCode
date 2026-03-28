class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        n=[int(i) for i in nums]
        n=sorted(n)
        return str(n[-(k)])
        