class Solution:
    def sortPeople(self,names,heights):
        res = sorted(zip(heights,names)) 
        return [res[i][1] for i in range(len(res)-1,-1,-1)]