class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        m1=max(salary)
        m2=min(salary)
        salary.remove(m1)
        salary.remove(m2)

        return float(sum(salary))/len(salary)
        