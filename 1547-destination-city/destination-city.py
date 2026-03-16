class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        seta=set()
        setb=set()
        for i in range(len(paths)):
            seta.add(paths[i][0])
            setb.add(paths[i][1])
        setc=setb-seta
        value = list(setc)[0]
        return value
        