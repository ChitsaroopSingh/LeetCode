class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        x= arrivalTime + delayedTime
        if x<24:
            return x
        elif x==24:
            return 0
        else:
            return x-24
        