class Solution(object):
    def minimumIndex(self, capacity, itemSize):
        min_cap=float('inf')
        ans=-1
        
        for i in range(len(capacity)):
            if capacity[i]>=itemSize and capacity[i]< min_cap:
                min_cap=capacity[i]
                ans=i     
        return ans