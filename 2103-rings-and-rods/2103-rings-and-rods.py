class Solution:
    def countPoints(self, rings: str) -> int:
        rods = ['','','','','','','','','','']
        res = 0
        if len(rings) < 7:
            return res
        for i in range(0,len(rings),2):
            rods[int(rings[i+1])] += rings[i]
        for rod in rods:
            if len(set(rod)) == 3:
                res += 1
            
        return res