class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res=[]
        IC=0
        DC=len(s)
        for i in s:
            if i =='I':
                res.append(IC)
                IC += 1
            else:
                res.append(DC)
                DC -= 1
        if s[-1] == 'I':
            res.append(IC)
        else:
            res.append(DC)
        return res