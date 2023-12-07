class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ptList =[[1]]
        
        for c in range(numRows-1):
            npt= [1]
            for i in range(1, c+1):
                npt.append(ptList[c][i-1]+ptList[c][i])
                
            npt.append(1)
            ptList.append(npt)
        return ptList
