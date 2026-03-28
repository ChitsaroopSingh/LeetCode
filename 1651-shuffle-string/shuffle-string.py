class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d=dict(zip(indices,s))

        sorted_d = dict(sorted(d.items()))

        result = ''.join([d[i] for i in sorted(d)])

        return result

        